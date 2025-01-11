import os
import asyncio
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

async def wait_until(dt):
    # sleep until the specified datetime
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())

async def run_at(dt, coro):
    await wait_until(dt)
    return await coro

async def hello():
    print('hello')


async def main():
    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    await handler.start_async()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_at(datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 16, 9), hello()))
    loop.run_forever()
    asyncio.run(main())

    