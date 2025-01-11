import os
import icalendar
import recurring_ical_events
import urllib.request
import datetime
import logging

SocketMode = True

from slack_bolt.async_app import AsyncApp

if SocketMode == True:
    #from slack_bolt.adapter.socket_mode import SocketModeHandler
    from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

from dotenv import load_dotenv
load_dotenv()

if SocketMode == True:
    app = AsyncApp(token=os.getenv("SLACK_BOT_TOKEN"))
else:
    app = AsyncApp(
        token=os.getenv("SLACK_BOT_TOKEN"),
        signing_secret=os.getenv("SLACK_SIGNING_SECRET")
    )

@app.event("app_mention")
async def Responce(event, say):
    welcome_channel_id = os.getenv('channel_id')
    user_id = event["user"]
    text = f"Hey, <@{user_id}>!"
    await say(text=text, channel=welcome_channel_id)

#if __name__ == "__main__":
    #if SocketMode == True:
        #SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
    #else:
        #app.start(port=int(3000))

async def main():
    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    await handler.start_async()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())