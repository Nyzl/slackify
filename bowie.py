import app
import string
import json
from urllib.request import urlopen
import re

def ziggy (payload):
  	if payload["event"]["type"] == "app_mention":
    	if "make a playlist" in payload["event"]["text"] or "create a playlist" in payload["event"]["text"] or "create playlist" in payload["event"]["text"] or "make playlist" in payload["event"]["text"]:
      	return {
        	"text":"So, ya wanna make a playlist, eh?",
        	"attachments":[{
          	"text": "",
          	"color": "#3AA3E3",
          	"attachment_type": "default",
          	"actions": [{
            	"name": "create_playlist",
            	"text": ":guitar: Let's go!",
            	"type": "button",
            	"value": "create_playlist"
            	}]
          	}]
        }
    
    else:
      	return "What?"

def major_tom (payload):
	if payload["type"] == "interactive_message":
		
		return {
			"trigger_id" : payload["trigger_id"],
            "dialog" : {
                "title": "Request a coffee",
                "submit_label": "Submit",
                "callback_id": user_id + "coffee_order_form",
                "elements": [
                    {
                        "label": "Coffee Type",
                        "type": "select",
                        "name": "meal_preferences",
                        "placeholder": "Select a drink",
                        "options": [
                            {
                                "label": "Cappuccino",
                                "value": "cappuccino"
                            },
                            {
                                "label": "Latte",
                                "value": "latte"
                            },
                            {
                                "label": "Pour Over",
                                "value": "pour_over"
                            },
                            {
                                "label": "Cold Brew",
                                "value": "cold_brew"
                            }
                        ]
                    }
                ]
            }
		}
		

if __name__ == "__main__":
    ziggy.run()
