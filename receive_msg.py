from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/sms", methods = ['GET','POST'])
def sms_reply():
	resp = MessagingResponse()
	resp.messages("I'm great too!")
	return str(resp)

if __name__ == "__main__":
	app.run() 