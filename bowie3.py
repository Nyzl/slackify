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
    if payload["type"] == "event_callback" and payload["event"]["type"] == "app_mention":
        if bool(re.search('(?:make|create).*playlist.*called', payload["event"]["text"])):
            name = re.search('(?<=called ).*',payload["event"]["text"])
            response["text"] = "So, ya wanna make a playlist, eh? called " + name
            response["attachments"] = ""
            return response
        else:
            response["text"] = "what do you want from me? Try calling your playlist something"
            response["attachments"] = ""
            return response

    else:
        text = str(payload)
        response["text"] = "what kind of thing was that"
        response["attachments"] = ""
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
