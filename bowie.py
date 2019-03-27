import app
import string
import json
from urllib.request import urlopen
import re

def ziggy(payload):
	if payload["event"]["type"] == "app_mention":
		if "make a playlist" in payload["event"]["text"] or "create a playlist" in payload["event"]["text"] or "create playlist" in payload["event"]["text"] or "make playlist" in payload["event"]["text"]:
			return {
				"text": "So, ya wanna make a playlist, eh?",
				"attachments": [{
					"text": "",
					"colour": "#3AA3E3",
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
			return {
				"text": "What?",
				"attachments": ""
			}
	elif payload["event"]["type"] == "member_joined_channel":
		user_id = payload["event"]["user"]
		channel_id = payload["event"]["channel"]
		return {
			"text": "Hey " + user_id + ", welcome to the " + channel_id,
			"attachments" : ""
		}

	else:
		return {
			"text": "What?",
			"attachments": ""
		}

if __name__ == "__main__":
	ziggy.run()
