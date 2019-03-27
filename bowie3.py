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
                message = payload["event"]["text"]
                if bool(re.search('(?>make|create).*playlist', message)):
                    response["text"] = "So, ya wanna make a playlist, eh?"
                    response["attachments"] = ""
                    return response
            response["text"] = "try asking me to create a playlist"
            response["attachments"] = ""
            return response

        else:
            response["text"] = "this is not an event_callback"
            response["attachments"] = ""
            return response
    except:
        response["text"] =  "nope"
        response["attachments"] = ""
        return response
