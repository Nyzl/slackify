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
    try:
        if payload["type"] == "event_callback":
            return "this was an event_callback"
        else:
            return "this is not an event_callback"
    except:
        return str(payload)
