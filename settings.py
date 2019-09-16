import os

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
