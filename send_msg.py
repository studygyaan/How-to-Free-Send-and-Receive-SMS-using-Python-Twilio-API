from twilio.rest import Client
from myTokens import account_sid, auth_token, my_phone_number

client = Client(account_sid, auth_token)

Client.message.create(
	to = my_phone_number,
	from_ = "+12029984713",
	body = "Hey there! How you doing?"
	)