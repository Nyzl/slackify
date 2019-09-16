import app,add_song,settings
import string,json,re,datetime,random
from urllib.request import urlopen

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
            response["text"] = settings.playlist_text
            response["attachments"] = settings.playlist_attachement
            return response
            # if someone tries to add a song
        elif bool(re.search('(?:add)', payload["event"]["text"])):
            song = add_song.addit(payload["event"]["text"])
            response["text"] = "I've added " + song + " to the playlist."
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
