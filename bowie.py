import app
import string
import json
from urllib.request import urlopen
import re

def ziggy (payload):
  if payload["type"] == "app_mention":
    return "i'm in the curve, man"
  else:
    #return "I'm confused"
    return str(payload["type"])
    

if __name__ == "__main__":
    ziggy.run()
