------------------------------------------------------------
 TWILIO CALL SERVICE – AI-DRIVEN VOICE INTERACTION
------------------------------------------------------------

This project enables automated outbound calls using the Twilio Voice API,
built with Flask. It captures real-time speech from users, processes responses,
and can optionally integrate with OpenAI for conversational AI capabilities.

------------------------------------------------------------
FEATURES
------------------------------------------------------------
- Outbound call initiation via Twilio REST API
- Real-time speech capture using Twilio’s AI speech engine
- Optional AI response generation using OpenAI GPT models
- RESTful endpoints for testing and integration
- Deployable on Glitch, Render, or locally with ngrok

------------------------------------------------------------
 PROJECT STRUCTURE
------------------------------------------------------------
twilio-call-service/
│
├── app.py              → Main Flask app
├── config_local.py     → Local Twilio credentials (ignored in production)
├── requirements.txt    → Project dependencies
├── Procfile            → Render deployment file
├── runtime.txt         → Python version for Render
├── start.sh            → Glitch startup script
└── README.txt          → This documentation

------------------------------------------------------------
 PREREQUISITES
------------------------------------------------------------
1. Python 3.11 or newer
2. Twilio Account: https://console.twilio.com
3. Twilio Voice-enabled phone number
4. (Optional) OpenAI API key for AI-driven replies

------------------------------------------------------------
SETUP INSTRUCTIONS
------------------------------------------------------------

1️⃣ Install dependencies
------------------------
pip install -r requirements.txt

2️⃣ Create config_local.py
--------------------------
Create a file named config_local.py in your project root:

TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token_here"
TWILIO_PHONE_NUMBER = "+1234567890"
BASE_URL = "https://your-public-url"

Never commit this file to GitHub (add it to .gitignore).

3️⃣ Run locally
---------------
python app.py

Visit http://127.0.0.1:3000
Expected output:
Twilio Call Service is running!

------------------------------------------------------------
🌐 USING NGROK FOR LOCAL TESTING
------------------------------------------------------------
Twilio requires a public HTTPS endpoint to reach your Flask app.

1. Download ngrok from https://ngrok.com/download
2. Authenticate:
   ngrok config add-authtoken YOUR_AUTH_TOKEN
3. Run:
   ngrok http 3000
4. Copy the public HTTPS URL (e.g. https://abc123.ngrok-free.app)
5. Update your config_local.py:
   BASE_URL = "https://abc123.ngrok-free.app"

Now Twilio can access your local app’s webhooks.

------------------------------------------------------------
API ENDPOINTS
------------------------------------------------------------
| Endpoint            | Method | Description                      |
|---------------------|---------|----------------------------------|
| /                   | GET     | Health check                     |
| /make-call          | POST    | Initiates a Twilio call          |
| /ask-question       | POST    | Plays voice prompt               |
| /process-answer     | POST    | Captures speech and responds     |
| /get-call-result    | GET     | Returns stored speech result     |
| /debug-creds        | GET     | Debug configuration values       |

------------------------------------------------------------
EXAMPLE REQUEST
------------------------------------------------------------
curl -X POST http://127.0.0.1:3000/make-call \
  -H "Content-Type: application/json" \
  -d "{\"toPhoneNumber\": \"+13315551234\"}"

Expected response:
{
  "message": "Call initiated successfully",
  "call_sid": "CAxxxxxxxxxxxxxxxxxxxxxxxx"
}

------------------------------------------------------------
DEPLOYMENT OPTIONS
------------------------------------------------------------

🔹 OPTION 1 — Render (Recommended)
----------------------------------
1. Push project to GitHub.
2. Go to https://render.com → “New Web Service”.
3. Connect your repo and set:
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
4. Add environment variables:

   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   BASE_URL=https://your-app-name.onrender.com
   (Optional) OPENAI_API_KEY=sk-your-openai-key

5. Deploy and test.
Your live app URL: https://your-app-name.onrender.com

------------------------------------------------------------
🔹 OPTION 2 — Glitch
------------------------------------------------------------
1. Go to https://glitch.com
2. Create a new project → "Hello Flask".
3. Replace files with:
   app.py, requirements.txt, start.sh, Procfile
4. Add a .env file:
   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   BASE_URL=https://your-glitch-project.glitch.me
5. Click “Show → In a New Window” to view the live app.

------------------------------------------------------------
🔹 OPTION 3 — Local (with ngrok)
------------------------------------------------------------
For testing without public deployment:
python app.py
ngrok http 3000

Update BASE_URL in config_local.py with the ngrok HTTPS URL.

------------------------------------------------------------
 AI INTEGRATION
------------------------------------------------------------
This service currently uses Twilio’s speech recognition AI to transcribe voice input.
You can extend it using OpenAI GPT for conversational logic.

Example:
from openai import OpenAI

ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
completion = ai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a polite assistant."},
        {"role": "user", "content": f"User said: {speech_result}"}
    ]
)
reply = completion.choices[0].message.content

------------------------------------------------------------
FUTURE ENHANCEMENTS
------------------------------------------------------------
1️⃣ AI Conversation Engine
   - Integrate GPT / Vertex AI for intelligent replies
2️⃣ Analytics Dashboard
   - Add call metrics and sentiment tracking
3️⃣ Agentic AI Workflow
   - Orchestrate multiple AI agents for automation
4️⃣ Scalable Cloud Architecture
   - Deploy on Kubernetes or GCP Cloud Run
5️⃣ Reusable Voice Gateway
   - Convert this into a plug-and-play AI voice interface

------------------------------------------------------------
DEPENDENCIES
------------------------------------------------------------
Flask==3.0.3
twilio==9.3.1
gunicorn==22.0.0
openai==1.42.0

------------------------------------------------------------
AUTHOR
------------------------------------------------------------
Chithra Ravi  
AI & Cloud Engineering Projects – 2025  
Twilio Voice + Flask integration for intelligent call automation.

------------------------------------------------------------



