import os
import icalendar
import recurring_ical_events
import urllib.request
import datetime
import logging

SocketMode = True

from slack_bolt import App

if SocketMode == True:
    from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv
load_dotenv()

if SocketMode == True:
    app = App(token=os.getenv("SLACK_BOT_TOKEN"))
else:
    app = App(
        token=os.getenv("SLACK_BOT_TOKEN"),
        signing_secret=os.getenv("SLACK_SIGNING_SECRET")
    )

#url = os.getenv('ical_link')
##Start_date = (2024, 1, 6)
##End_date = (2024, 1, 7)
#a_time = (2024, 1, 6)
#
#ical_string = urllib.request.urlopen(url).read()
#calendar = icalendar.Calendar.from_ical(ical_string)
##events = recurring_ical_events.of(calendar).between(Start_date, End_date)
#events = recurring_ical_events.of(calendar).at(a_time)

#for event in events:
#    name = event["SUMMARY"]
#    start = event["DTSTART"].dt
#
#    try:
#        description = event["DESCRIPTION"]
#    except:
#        description = "N/A" 
#
#    try:
#        location = event["LOCATION"]
#    except:
#        location = "N/A" 
#
#    print("{} at {} begins at {} - {}".format(name, location, start, description))   

@app.event("app_mention")
def Responce(event, say):
    welcome_channel_id = os.getenv('channel_id')
    user_id = event["user"]
    text = f"Hey, <@{user_id}>!"
    say(text=text, channel=welcome_channel_id)

if __name__ == "__main__":
    if SocketMode == True:
        SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
    else:
        app.start(port=int(3000))