from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    print(request.form)
    msg = request.form.get('Body')
    sender = request.form.get('From')

    # Create reply
    resp = MessagingResponse()
    # reply, reply_type = fetch_reply(msg, sender)
    # if reply_type=='text':
    #     resp.message(reply)
    #     return str(resp)
    
    resp.message(fetch_reply(msg, sender))
    # resp.message("You said: {}".format(msg))
                    #.media('https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)