from twilio.rest import Client 
 
account_sid = 'AC842cdb38711123bf6bf6e62a57af059c' 
auth_token = 'f9f8ab555aca66793581a0d33f2f616d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hey Baby! What are you doin? I miss you so much!',      
                              to='whatsapp:+919021393816' 
                        ) 
 
print(message.sid)