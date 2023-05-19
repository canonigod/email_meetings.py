import smtplib
import ssl
import datetime
import time
import pytz

# Set the desired timezone
timezone = pytz.timezone('EST')

# Get the current date and time in the specified timezone
current_datetime = datetime.datetime.now(timezone)

# Get the day of the week (week name)
week_name = current_datetime.strftime('%A')

# SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For SSL/TLS, use port 465

# Gmail account details
sender_email = "sender_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_pw"

# Email message
subject = f"My Meetings Today({week_name})"

meetings_of_week = [
    {
        "day": "Monday",
        "text": "I have meetings today at the following times:\n\n - 11:30am (team meeting. Important!!) \n - 2:00pm (not important)"
    },
    {
        "day": "Tuesday",
        "text": "I have meetings today at the following times:\n\n - 10:30am (not important) \n - 11:30am (team meeting. Important!!)"
    },
    {
        "day": "Wednesday",
        "text": "I have meetings today at the following times:\n\n - 11:30am (team meeting. Important!!) \n - 2:00pm (not important)"
    },
    {
        "day": "Thursday",
        "text": "I have meetings today at the following times:\n\n - 10:30am (not important) \n - 11:30am (team meeting, important)"
    },
    {
        "day": "Friday",
        "text": "I have meetings today at the following times:\n\n - 11:30am (team meeting. Important!!)"
    }
]

meeting_day_text_info = '';

print('started...')
# Accessing the array elements
for day in meetings_of_week:
    if day["day"] == week_name:
        meeting_day_text_info = day["text"]
        break

try:
    # Create an insecure SSL context
    context = ssl._create_unverified_context()

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)

        # Construct the email message
        message = f"Subject: {subject}\n\n{meeting_day_text_info}"

        # Send the email
        server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred while sending the email: {str(e)}")