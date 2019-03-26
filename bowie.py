#built on the brilliant work by Adam J Calhourn from his post
#https://medium.com/@neuroecology/punctuation-in-novels-8f316d542ec4#.tz6i4h1ub

import app
import string
import json
from urllib.request import urlopen
import re

def ziggy (payload):
  
  if payload.event.type == "app_mention":
    #if "make a playlist" in payload.event.text
    #or "make playlist" in payload.event.text or "create a playlist" in payload.event.text or "create playlist" in payload.event.text:
    elif payload.event.text == "Hello":
      return "So, you wanna make a playlist eh?"

if __name__ == "__main__":
    ziggy.run()