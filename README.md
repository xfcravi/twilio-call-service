# Twilio Call Service

A Flask-based microservice for initiating and managing Twilio voice calls.  
Designed as a Gen AI POC demonstrating automated voice interactions and real-time speech recognition.

---

## Features

- Outbound voice calls via Twilio API  
- Real-time speech input capture  
- Secure environment configuration  
- Supports Glitch and Heroku deployments  

---

## Setup Instructions

1. Clone the repo  
   ```bash
   git clone https://github.com/<yourrepo>/twilio-call-service.git
   cd twilio-call-service

2. Create .env file
 cp .env.example .env

3. Install dependencies

    pip install -r requirements.txt

4. Run locally

python app.py

5. Expose to Twilio (e.g., via ngrok)
ngrok http 3000

## API Endpoints
Endpoint	        Method	    Description
/make-call	        POST	    Initiates outbound call
/ask-question	    POST	    Twilio callback endpoint
/process-answer	    POST	    Processes speech input
/get-call-result    GET	        Fetches recorded response

### On **Glitch**
1. Upload all files.
2. Add `.env` variables under “Secrets”.
3. Ensure `glitch.json` is present.
4. App auto-starts at `https://<project>.glitch.me`.

### On **Heroku**
1. `heroku create twilio-call-service`
2. `heroku config:set TWILIO_ACCOUNT_SID=... TWILIO_AUTH_TOKEN=... TWILIO_PHONE_NUMBER=... BASE_URL=https://your-app.herokuapp.com`
3. `git push heroku main`

