import re
import requests,os,json,base64,urllib
from flask import request

def addit(message):

    #what's the song we want to add
    song_search = re.search(r'(?<=add).*$', message)
    song = song_search.group(0)
    #do all the spotify authentication stuff
    # Auth Step 4: Requests refresh and access tokens
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
    SPOTIFY_API_BASE_URL = "https://api.spotify.com"
    API_VERSION = "v1"
    SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)
    CHANNEL_MUSIC = "C0B6CHKSL"
    CHANNEL_DEV = "CH02K9AEA"
    CHANNEL_ID = CHANNEL_DEV


    CLIENT_SIDE_URL = "http://127.0.0.1"
    SERVER_SIDE_URL = "https://slackifybot.herokuapp.com"
    PORT = 8080
    REDIRECT_URI = "{}/callback/q".format(SERVER_SIDE_URL)
    SCOPE = "playlist-modify-public playlist-modify-private"
    STATE = ""
    SHOW_DIALOG_bool = True
    SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        # "state": STATE,
        # "show_dialog": SHOW_DIALOG_str,
        "client_id": CLIENT_ID
    }
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    url_args = "&".join(["{}={}".format(key,urllib.parse.quote(val)) for key,val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"


    # Auth Step 6: Use the access token to access Spotify API and search
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
    authorization_header["Content-Type"] = "application/json"
    data = {}
    data["q"] = song
    data["type"] = 'track'
    data["limit"] = 1
    payload = json.dumps(data)

    search = requests.get('https://api.spotify.com/v1/search', headers=authorization_header, data=payload)

    search_result = json.loads(search.text)

     #add the result of the search to the playlist
    SPOTIFY_API_BASE_URL = "https://api.spotify.com"
    API_VERSION = "v1"
    SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])

    songs_to_add = search_result["tracks"]["items"]["uri"]

    add_the_song = requests.post(playlist_api_endpoint, headers=authorization_header, data=songs_to_add)

    return search_result["name"]
