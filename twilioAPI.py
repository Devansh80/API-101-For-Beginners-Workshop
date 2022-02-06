# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token ='8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Congrats, this api is working fine !",
                     from_='+1912xxxx',
                     to='+9188xxxxxx'
                 )

print(message.sid)
