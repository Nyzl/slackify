#all the json elements Slack wants
import os,random

playlist_text = "So, ya wanna make a playlist, eh?"
playlist_attachement = [
                {
                    "blocks": [
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":guitar: Let's go!"
                                        },
                                    "value": "create_playlist",
                                    "action_id":"playlist_button"
                                }
                            ]
                        }
                    ]
                }
            ]

mention_text_list = [
    "hi, it's a wonderful day to be alive isn't it",
    "i wonder what this weeks playlist theme will be",
    "did you know, my first word was 'goose'",
    "don't worry, i'm not sentient, these are just words someone told me to say....or did they!",
    "What's up?"
    ]

mention_text = random.choice(mention_text_list)
