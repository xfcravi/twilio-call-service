# app.py
import os
from flask import Flask, request, jsonify, Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# ✅ Load Twilio credentials from a separate local config file
try:
    from config_local import (
        TWILIO_ACCOUNT_SID,
        TWILIO_AUTH_TOKEN,
        TWILIO_PHONE_NUMBER,
        BASE_URL,
    )
except ImportError:
    raise Exception(
        "Missing config_local.py file. Please create it with your Twilio credentials."
    )

app = Flask(__name__)

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Temporary storage for speech recognition results
call_results = {}


@app.route("/")
def home():
    return "✅ Twilio Call Service is running!"


@app.route("/make-call", methods=["POST"])
def make_call():
    data = request.get_json()
    to_number = data.get("toPhoneNumber")
    if not to_number:
        return jsonify({"error": "Missing 'toPhoneNumber' field"}), 400

    try:
        call = client.calls.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            url=f"{BASE_URL}/ask-question",
        )
        call_results[call.sid] = None
        return jsonify(
            {"message": "Call initiated successfully", "call_sid": call.sid}
        ), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ask-question", methods=["POST"])
def ask_question():
    response = VoiceResponse()
    with response.gather(
        input="speech", action="/process-answer", method="POST"
    ) as gather:
        gather.say(
            "Hello! This is Chithra from Gen AI Proof of Concept. Please say your name after the beep."
        )
    return Response(str(response), mimetype="application/xml")


@app.route("/process-answer", methods=["POST"])
def process_answer():
    call_sid = request.form.get("CallSid")
    speech_result = request.form.get("SpeechResult")

    if call_sid:
        call_results[call_sid] = speech_result

    response = VoiceResponse()
    if speech_result:
        response.say(f"Thank you! You said your name is {speech_result}. Have a great day!")
    else:
        response.say("Sorry, I didn’t catch that. Goodbye.")
    return Response(str(response), mimetype="application/xml")


@app.route("/get-call-result", methods=["GET"])
def get_call_result():
    call_sid = request.args.get("call_sid")
    result = call_results.get(call_sid)
    if result is None:
        return jsonify({"error": "No result found"}), 404
    return jsonify({"call_sid": call_sid, "speech_result": result})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
