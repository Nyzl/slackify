import app
import string
import json
from urllib.request import urlopen
import re

def ziggy (payload):
  if payload["event"]["type"] == "app_mention":
    if "make a playlist" or "create a playlist" in payload["event"]["text"]:
      return "So, ya wanna make a playlist, eh?"
    else:
      return "i'm in the curve, man"

if __name__ == "__main__":
    ziggy.run()
