import requests
import app

def slack_post(response):
    payload = {
    "channel": CHANNEL_ID,
    "token": str(BOT_USER_TOKEN),
    "text": response["text"],
    "attachments": response["attachments"]
    }

    headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=json.dumps(payload))

    return "you can close this now"