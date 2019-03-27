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
			"text": "Hey @" + user_id + ", welcome to the #music channel\n\nEvery Friday we have a theme. We add music to a collaborative playlist on Spotify that matches this theme. Highlights include \"Songs on Donald Trumps iPod\"\n\nI'm also here to help out with making the playlist. You can say hello to me by mentioning me and I'll respond to you. For now I'm a bit dumb, but I'll get smarter, I promise.\n\nIf you mention me and ask me to create a playlist I'll do this for you. All you need to do is tell me the name and theme and job's a good'un.",
			"attachments" : ""
		}

	else:
		return {
			"text": "What?",
			"attachments": ""
		}

if __name__ == "__main__":
	ziggy.run()
