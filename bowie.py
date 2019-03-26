import app
import string
import json
from urllib.request
import urlopen
import re

def ziggy(payload):
  if payload["event"]["type"] == "app_mention":
  if "make a playlist" in payload["event"]["text"] or "create a playlist" in payload["event"]["text"] or "create playlist" in payload["event"]["text"] or "make playlist" in payload["event"]["text"]:
  return {
    "text": "So, ya wanna make a playlist, eh?",
    "attachments": [{
      "text": "",
      "color": "#3AA3E3",
      "attachment_type": "default",
      "actions": [{
        "name": "create_playlist",
        "text": ":guitar: Let's go!",
        "type": "button",
        "value": "create_playlist"
      }]
    }]
  }

else :
  return "What?"

if __name__ == "__main__":
  ziggy.run()