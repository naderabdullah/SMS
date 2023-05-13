from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC624b221a7590f78aa83ed1aca45ad268"
# Your Auth Token from twilio.com/console
auth_token  = "b74d1b1f1975fb64de24243bae95e6b9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19144135270", 
    from_="+13478096147",
    body="Hello")

print(message.sid)