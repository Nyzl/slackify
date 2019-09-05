import re
import requests,os,json,base64,urllib
import spotipy
from flask import request
from spotipy.oauth2 import SpotifyClientCredentials

def addit(message):

    #what's the song we want to add
    song_search = re.search(r'(?<=add).*$', message)
    song = song_search.group(0)
    print(song)

    # Auth Step 6: access Spotify API and search

    client_credentials_manager = SpotifyClientCredentials(client_id=app.CLIENT_ID, client_secret=app.CLIENT_SECRET)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    search_result = spotify.search(q=song, limit=1, offset=0, type='track', market=None)

     #add the result of the search to the playlist

    songs_to_add = search_result["tracks"]["items"]["uri"]

    add_the_song = spotify.user_playlist_add_tracks(app.CLIENT_ID, app.playlist_data["external_urls"], songs_to_add, position=None)

    return search_result["name"]
