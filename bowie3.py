import app
import string
import json
from urllib.request import urlopen
import re
import datetime
import random
import add_song

# work out what time of day it is
currentTime = datetime.datetime.now()
currentTime.hour
0
if currentTime.hour < 12:
  time = ("Good morning")
elif 12 <= currentTime.hour < 18:
  time = ("Good afternoon")
else:
  time = ("Good evening")


def ziggy(payload, url):
    response = {"text":"","attachments":""}
    if payload["event"]["type"] == "app_mention":

        if bool(re.search('(?:make|create|haz).*playlist', payload["event"]["text"])):
            response["text"] = "So, ya wanna make a playlist, eh?"
            response["attachments"] = [
                {
                    "blocks": [
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":guitar: Let's go!"
                                        },
                                    "value": "create_playlist",
                                    "action_id":"playlist_button"
                                }
                            ]
                        }
                    ]
                }
            ]
            return response
            # if someone tries to add a song
        elif bool(re.search('(?:add)', payload["event"]["text"])):
            #print(payload["event"]["text"])
            song = add_song.addit(payload["event"]["text"])
            response["text"] = "I've added " + song + " to the playlist."
            print(response["text"])
            return response
        else:
            response["text"] = time + "! What's up?"

            return response

    elif payload["event"]["type"] == "member_joined_channel":
        response["text"] = time + "! Welcome to the #music channel :wave: :guitar:"
        return response

    else:
        text = str(payload)

        response["text"] = "What the heck was that?"

        return response
