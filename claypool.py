import app, string, json, re, requests
from urllib.request import urlopen

def les ():
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=json.dumps(payload))


if __name__ == "__main__":
    les.run()
