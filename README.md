# slackify
This was a Firebreak project within the Customer Journey team at Citizens Advice. 

Build a Slackbot that will interact with Spotify for the teams weekly colaborative Friday playlists.

Built in Python 3.7.4 previously deployed to Heroku, now on Google Cloud Run

.envrc is used to store env variables for local use and .env.yaml is used to store them for Cloud Run....i hate that they are in two places

# Deploy
Thge makefile handles building and deploying
`make build`
and
`make deploy`
