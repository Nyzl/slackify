import app
import string
import json
from urllib.request import urlopen
import re
import datetime
import random

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
    response = {"name":"","text":"","attachments":""}
    if payload["type"] == "event_callback" and payload["event"]["type"] == "app_mention":
        if bool(re.search('(?:make|create|haz).*playlist.*called', payload["event"]["text"])):
            name = re.search('(?<=called ).*',payload["event"]["text"]).group()
            response["name"] = name
            response["text"] = "So, ya wanna make a playlist, eh?\n\n I've made you one called \"" + name + "\"\n\nClick this link to open in Spotify: " + url
            response["attachments"] = ""
            return response
        else:
            response["text"] = "What do you want from me? Try calling your playlist something"
            response["attachments"] = ""
            return response

    elif payload["event"]["type"] == "member_joined_channel":
        response["text"] = time + "! Welcome to the #music channel :wave: :guitar:"
        response["attachments"] = ""
        return response

    else:
        text = str(payload)
        response["text"] = "What the heck was that?"
        response["attachments"] = ""
        return response
