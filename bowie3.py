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


def ziggy(payload):
    response = {}
    if payload["type"] == "event_callback" and payload["event"]["type"] == "app_mention" and bool(re.search('(make|create).*playlist', payload["event"]["text"])):
        response["text"] = "So, ya wanna make a playlist, eh?"
        response["attachments"] = ""
        return response

    else:
        str = str(payload)
        response["text"] = "what kind of thing was that, it wasn't an event_callback & app_mention  -  "+str.replace("@Slackify", "xxx")
        esponse["attachments"] = ""
        return response
    # try:
    #     if payload["type"] == "event_callback":
    #         if payload["event"]["type"] == "app_mention":
    #             message = payload["event"]["text"]
    #             if bool(re.search('(?>make|create).*playlist', message)):
    #                 response["text"] = "So, ya wanna make a playlist, eh?"
    #                 response["attachments"] = ""
    #                 return response
    #         response["text"] = "try asking me to create a playlist"
    #         response["attachments"] = ""
    #         return response
    #
    #     else:
    #         response["text"] = "this is not an event_callback"
    #         response["attachments"] = ""
    #         return response
    # except:
    #     response["text"] =  "nope"
    #     response["attachments"] = ""
    #     return response
