from twilio.rest import Client
import datetime
import pytz

# Set the desired timezone
timezone = pytz.timezone('EST')

# Get the current date and time in the specified timezone
current_datetime = datetime.datetime.now(timezone)

# Get the day of the week (week name)
week_name = current_datetime.strftime('%A')

meetings_of_week = [
    {
        "day": "Monday",
        "text": "David's meetings today are the following times:\n\n - 11:30am  (important!!) \n - 2:00pm (not important)"
    },
    {
        "day": "Tuesday",
        "text": "David's meetings today are the following times:\n\n - 10:30am (not important) \n - 11:30am  (important!!)"
    },
    {
        "day": "Wednesday",
        "text": "David's meetings today are the following times:\n\n - 11:30am  (important!!) \n - 2:00pm (not important)"
    },
    {
        "day": "Thursday",
        "text": "David's meetings today are the following times:\n\n - 10:30am (not important) \n - 11:30am (team meeting, important)"
    },
    {
        "day": "Friday",
        "text": "David's meetings today are the following times:\n\n - 11:30am  (important!!)"
    }
]

meeting_day_text_info = ''

# Accessing the array elements
for day in meetings_of_week:
    if day["day"] == week_name:
        meeting_day_text_info = day["text"]
        break

# Twilio account SID and authentication token
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_ACCOUNT_TOKEN'

# Twilio phone number and recipient's phone number
twilio_number = '+1YOUR_TWILIO_PHONE_NUMBER'
recipient_number = '+1YOUR_RECEPIENT_PHONE_NUMBER'  # Include the country code

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
message = client.messages.create(
    body=meeting_day_text_info,
    from_='whatsapp:' + twilio_number,
    to='whatsapp:' + recipient_number
)

# Print the message SID
print('Message SID:', message.sid)
