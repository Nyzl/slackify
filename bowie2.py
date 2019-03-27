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


def ziggy(payload, request):
    response = {}
    try:
        if payload["type"] == "event_callback":
            if payload["event"]["type"] == "app_mention":
                if "make a playlist" in payload["event"]["text"] or "create a playlist" in payload["event"]["text"] or "create playlist" in payload["event"]["text"] or "make playlist" in payload["event"]["text"]:
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
        									"value": "create_playlist"
        								}
        							]
        						}
        					]
        				}
        			]
                    return response
            response["text"] = "this was an event_callback: "+str(request)
            response["attachments"] = ""
            return response


        else:
            response["text"] = "this is not an event_callback"
            response["attachments"] = ""
            return response
    except:
        response["text"] =  str(request)
        response["attachments"] = ""
        return response
