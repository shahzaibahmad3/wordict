from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from mean import getmean

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/sms', methods=['POST'])
def sms_reply():
    word = request.form.get('Body')
    
    msg_body = getmean(word)
    #print(msg_body)
    resp = MessagingResponse()
    resp.message("word: "+word+"\n\n"+msg_body)
    
    return str(resp)


if __name__ == "__main__" :
    app.run(debug = True)
    
    
    
