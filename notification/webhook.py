### forward notifications via a POST to a webhook URL, useful for integrating with IFTTT or Zapier
## HOW IT WORKS: the notification is sent in a JSON format to the webhook URL with a HTTP POST request
## DEPENDENCIES:
# OS:
# Python: 
## CONFIGURATION:
# required: "url"
# optional: 
## COMMUNICATION:
# INBOUND: 
# - NOTIFY: receive a notification request
# OUTBOUND: 

import json
import requests

from sdk.python.module.notification import Notification

import sdk.python.utils.web
import sdk.python.utils.exceptions as exception

class Webhook(Notification):
    # What to do when initializing
    def on_init(self):
        # configuration settings
        self.house = {}
        # require configuration before starting up
        self.config_schema = 1
        self.add_configuration_listener("house", 1, True)
        self.add_configuration_listener(self.fullname, "+", True)

    # What to do when running
    def on_start(self):
        pass
        
    # What to do when shutting down
    def on_stop(self):
        pass

    # What to do when ask to notify
    def on_notify(self, severity, text):
        # build the data payload to send to the webhook
        data = {}
        house_name_key = self.config["house_name_key"] if "house_name_key" in self.config else "house_name"
        severity_key = self.config["severity_key"] if "severity_key" in self.config else "severity"
        message_key = self.config["message_key"] if "message_key" in self.config else "message"
        data[house_name_key] = self.house["name"]
        data[severity_key] = severity
        data[message_key] = text
        data = json.dumps(data)
        self.log_debug("Request: "+str(data))
        # send the notification to the webhook
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url=self.config["url"], headers=headers, data=data)
            response.raise_for_status()
        except Exception,e: 
            self.log_warning("unable to notify: "+exception.get(e))
            return
        self.log_debug("Response: "+str(response.text))

     # What to do when receiving a new/updated configuration for this module    
    def on_configuration(self, message):
        if message.args == "house" and not message.is_null:
            if not self.is_valid_configuration(["name"], message.get_data()): return False
            self.house = message.get_data()
        # module's configuration
        if message.args == self.fullname and not message.is_null:
            if message.config_schema != self.config_schema: 
                return False
            if not self.is_valid_configuration(["url"], message.get_data()): return False
            self.config = message.get_data()