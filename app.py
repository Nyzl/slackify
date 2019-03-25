from flask import Flask,render_template,request,redirect
import requests, os
import bowie

app = Flask(__name__)

app.vars={}

@app.route('/',methods=['GET'])
def deftones():
        return "you GETTED me"

@app.route('/slack',methods=['POST'])
def weezer():
    payload = request.get_json()
    response = bowie.ziggy(payload)
    sendToSlack(response)
    #return str(payload["challenge"])


def sendToSlack(response):
    BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
    payload = {'text': response, 'channel': 'CH02K9AEA'}
    headers = {'Content-type': 'application/json', 'Authorization':'Bearer '+BOT_USER_TOKEN}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=payload)




if __name__ == "__main__":
    app.run()
