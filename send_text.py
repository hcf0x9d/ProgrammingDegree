from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd8930eee09b376db0f6df655e5354d4d"
# Your Auth Token from twilio.com/console
auth_token  = "6158d9f9450c6519c8a38d0f47160f87"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+12066170650",
    from_ = "+13609002074",
    body = "Hello from Python!")

print(message.sid)