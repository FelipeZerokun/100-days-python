import os
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.twilio_SID = os.environ['MY_TWILIO_SID']
        self.twilio_token = os.environ['MY_TWILIO_TOKEN']
        self.twilio_num = os.environ['MY_TWILIO_NUM']
        self.my_num = os.environ['MY_PERSONAL_NUM']
        self.client = Client(self.twilio_SID, self.twilio_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_num,
            to=self.my_num,
        )
        # Prints if successfully sent.
        print(message.sid)
