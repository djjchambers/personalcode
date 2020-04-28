from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
    return str(resp)
    
if __name__ == "__main__":
    app.run()