from twilio.rest import Client
from django.conf import settings
import os

# account_sid = settings.TWILIO_ACCOUNT_SID
# auth_token = settings.TWILIO_AUTH_TOKEN
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+61488839814',
    to='+61423083811',
    # to='+61424807835',
    body='Hello from django',
)

print(message.sid)
