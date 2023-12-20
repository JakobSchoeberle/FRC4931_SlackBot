import os
import icalendar
import recurring_ical_events
import urllib.request
import datetime
import logging
import schedule

from slack_bolt import App
from dotenv import load_dotenv

# Initialize the app with the bot token and signing secret
load_dotenv()
app = App(
    token = os.getenv('SLACK_BOT_TOKEN'),
    signing_secret = os.getenv('SLACK_SIGNING_SECRET')
)

url = "https://calendar.google.com/calendar/ical/frc4931%40gmail.com/public/basic.ics"
#Start_date = (2024, 1, 6)
#End_date = (2024, 1, 7)
a_time = (2024, 1, 6)

ical_string = urllib.request.urlopen(url).read()
calendar = icalendar.Calendar.from_ical(ical_string)
#events = recurring_ical_events.of(calendar).between(Start_date, End_date)
events = recurring_ical_events.of(calendar).at(a_time)

for event in events:
    name = event["SUMMARY"]
    start = event["DTSTART"].dt

    try:
        description = event["DESCRIPTION"]
    except:
        description = "N/A" 

    try:
        location = event["LOCATION"]
    except:
        location = "N/A" 

    print("{} at {} begins at {} - {}".format(name, location, start, description))   

# Add functionality here
# @app.event("app_home_opened") etc.
    
# Create a timestamp for tomorrow at 9AM
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
scheduled_time = datetime.time(hour=9, minute=30)
schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')

# Channel you want to post message to
channel_id = "C12345"

try:
    # Call the chat.scheduleMessage method using the WebClient
    result = client.chat_scheduleMessage(
        channel=channel_id,
        text="Hello World!",
        post_at=schedule_timestamp
    )
    # Log the result
    logging.info(result)

except SlackApiError as e:
    logging.error("Error scheduling message: {}".format(e))


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))