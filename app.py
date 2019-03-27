from flask import Flask,render_template,request,redirect,g
import requests,os,json,base64,urllib
import bowie,bowie2,bowie3
from boto.s3.connection import S3Connection
import urllib

app = Flask(__name__)
app.vars={}

@app.route('/',methods=['GET'])
def deftones():
        return "you GETTED me"

@app.route('/slack',methods=['POST'])
def weezer():
    BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
    in_payload = request.get_json()
    response = bowie3.ziggy(in_payload)

    out_payload = {
    "channel": "CH02K9AEA",
    "token": str(BOT_USER_TOKEN),
    "text": response["text"],
    "attachments": response["attachments"]
    }

    headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=json.dumps(out_payload))
    return str(r.text)


if __name__ == "__main__":
    app.run()
