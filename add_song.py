import re
import requests,os,json,base64,urllib
import client
from flask import request

def addit(message):

    #what's the song we want to add
    song_search = re.search(r'(?<=add).*$', message)
    song = song_search.group(0)


    # Auth Step 6: access Spotify API and search

    search_result = client.Spotify.search(song, limit=1, offset=0, type='track', market=None)

     #add the result of the search to the playlist

    songs_to_add = search_result["tracks"]["items"]["uri"]

    add_the_song = client.Spotify.user_playlist_add_tracks(app.CLIENT_ID, app.playlist_data["external_urls"], songs_to_add, position=None)

    return search_result["name"]
