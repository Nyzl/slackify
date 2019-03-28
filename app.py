from flask import Flask,render_template,request,redirect,g
import requests,os,json,base64,urllib
import bowie,bowie2,bowie3
from boto.s3.connection import S3Connection

app = Flask(__name__)
app.vars={}

# Spotify Client Keys
CLIENT_ID = os.environ['SP_CLIENT_ID']
CLIENT_SECRET = os.environ['SP_CLIENT_SECRET']

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
SERVER_SIDE_URL = "https://slackifybot.herokuapp.com"
PORT = 8080
#REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
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

playlist_name = "holder"

@app.route('/',methods=['GET'])
def deftones():
        return "you GETTED me"

@app.route('/slack',methods=['POST'])
def weezer():
    #SPOTIFY authentication
    global playlist_name
    url_args = "&".join(["{}={}".format(key,urllib.parse.quote(val)) for key,val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)

    BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
    in_payload = request.get_json()
    response = bowie3.ziggy(in_payload, auth_url)
    playlist_name = response["name"]

    out_payload = {
    "channel": "CH02K9AEA",
    "token": str(BOT_USER_TOKEN),
    "text": response["text"],
    "attachments": response["attachments"]
    }

    headers = {"Content-type":"application/json;charset=utf-8", "Authorization":"Bearer "+ str(BOT_USER_TOKEN)}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, data=json.dumps(out_payload))
    return str(r.text)

@app.route("/callback/q")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
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

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}

    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    authorization_header["Content-Type"] = "application/json"
    data = {"name":"A New Playlist"}

    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    #playlist_api_endpoint = "https://api.spotify.com/v1/users/xu15ggjeufiorfq5pozsze64z/playlists"
    playlists_response = requests.post(playlist_api_endpoint, headers=authorization_header, data=json.dumps(data))
    playlist_data = playlists_response.text

    return str(playlist_data) + playlist_name

if __name__ == "__main__":
    app.run()
