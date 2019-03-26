from flask import Flask,render_template,request,redirect
import requests, os, json
import bowie
from boto.s3.connection import S3Connection

app = Flask(__name__)
app.vars={}

@app.route('/',methods=['GET'])
def deftones():
    return "you GETTED me"

@app.route('/slack',methods=['POST'])
def weezer():
    BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
    payload = request.get_json()
    response = bowie.ziggy(payload)

    payload = {"text":response["text"], "attachments":response["attachments"] ,"channel":"CH02K9AEA"}
    headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=json.dumps(payload))

    return str(r.text)

#@app.route("/slack",methods=['POST'])
#def tame_impala():
#	BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
#  	payload = request.get_json()
#    response = bowie.major_tom(payload)
	
#	payload = {"trigger_id":payload["trigger_id"], "dialog":payload["dialog"]}
#	headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
#	r = requests.post("https://slack.com/api/dialog.open", headers=headers, data=json.dumps(payload))
	
#	return "Tame Impala"
  
if __name__ == "__main__":
    app.run()
