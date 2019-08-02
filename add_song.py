import re
import requests,os,json,base64,urllib
from flask import request

def addit(message):

    #what's the song we want to add
    song_search = re.search(r'(?<=add).*$', message)
    song = song_search.group(0)
    #do all the spotify authentication stuff
    # Auth Step 4: Requests refresh and access tokens
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
    auth_token = request.args['code']
    print(auth_token)
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    data = "{}:{}".format(CLIENT_ID, CLIENT_SECRET)
    base64encoded = base64.b64encode(data.encode())
    headers = {"Authorization": "Basic {}".format(base64encoded.decode())}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

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
