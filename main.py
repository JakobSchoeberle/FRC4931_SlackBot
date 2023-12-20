import os
import icalendar
import recurring_ical_events
import urllib.request
import schedule

#from slack_bolt import App
#from dotenv import load_dotenv

# Initialize the app with the bot token and signing secret
#load_dotenv()
#app = App(
#    token = os.getenv('SLACK_BOT_TOKEN'),
#    signing_secret = os.getenv('SLACK_SIGNING_SECRET')
#)

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


#if __name__ == "__main__":
#    app.start(port=int(os.environ.get("PORT", 3000)))