import app
import string
import json
from urllib.request
import urlopen
import re

<<<<<<< HEAD
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

		else:
  			return "What?"
=======
def ziggy (payload):
  if payload["event"]["type"] == "app_mention":
    if "make a playlist" in payload["event"]["text"] or "create a playlist" in payload["event"]["text"] or "create playlist" in payload["event"]["text"] or "make playlist" in payload["event"]["text"]:
      return {
        "text":"So, ya wanna make a playlist, eh?",
        "attachments":[{
          "text": "",
          "color": "#3AA3E3",
          "attachment_type": "default",
          "actions": [{
            "name": "coffee_order",
            "text": ":coffee: Order Coffee",
            "type": "button",
            "value": "coffee_order"
            }]
          }]
        }
    
    else:
      return "What?"
>>>>>>> parent of b1d44fa... Update bowie.py

if __name__ == "__main__":
  ziggy.run()