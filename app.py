from flask import Flask,render_template,request,redirect
import requests, os, json
import bowie, bowie2
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
    response = bowie2.ziggy(in_payload)

    payload = {
    "channel": "CH02K9AEA",
    "token": str(BOT_USER_TOKEN),
    "text": response
    }

    # if in_payload["event"]["type"] == "block_actions":
    #     trigger_id = payload["trigger_id"]
    #     out_payload = {
    #         "trigger_id": trigger_id,
    #         "dialog":{
    #             "title": "Request a coffee",
    #             "submit_label": "Submit",
    #             "callback_id": "",
    #             "elements": [
    #                 {
    #                     "label": "Coffee Type",
    #                     "type": "select",
    #                     "name": "meal_preferences",
    #                     "placeholder": "Select a drink",
    #                     "options": [
    #                         {
    #                             "label": "Cappuccino",
    #                             "value": "cappuccino"
    #                         },
    #                         {
    #                             "label": "Latte",
    #                             "value": "latte"
    #                         },
    #                         {
    #                             "label": "Pour Over",
    #                             "value": "pour_over"
    #                         },
    #                         {
    #                             "label": "Cold Brew",
    #                             "value": "cold_brew"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     }
    #
    #     r = requests.post(urllib.parse.quote("https://slack.com/api/dialog.open?token="+BOT_USER_TOKEN+"&dialog="+out_payload+"&trigger_id="+trigger_id))
    #     return str(r.text)
    #
    # else:
    #
    #     payload = {
    #         "channel": "CH02K9AEA",
    #         "token": str(BOT_USER_TOKEN),
    #         "text": response["text"],
    #         "attachments": response["attachments"]
    #     }
    #     headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
    #     r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=json.dumps(payload))

        return str(r.text)

if __name__ == "__main__":
    app.run()
