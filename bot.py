# import from external libraries
import os
import ipdb  # equivalent to Ruby's Pry - add `ipdb.set_trace()` where needed to inspect scoped variables etc
from dotenv import load_dotenv
from twitchio.ext import commands

# import everything imported in functions.py - after adding a new
# function file, be sure to import the file in functions.py
from functions import *

dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv_path = os.path.join(dir_path, ".env")
load_dotenv(dotenv_path)

# get credentials
TMI_TOKEN = os.environ.get("TMI_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")
BOT_NICK = os.environ.get("BOT_NICK")
BOT_PREFIX = os.environ.get("BOT_PREFIX")
CHANNELS = os.environ.get("CHANNELS").split(",")

# set path to file where data are stored
JSON_FILEPATH = str(os.path.dirname(os.path.realpath(__file__))) + "/data.json"

# initialise bot
bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNELS,
)

# hooks for bot loading and messages being sent in chat
@bot.event
async def event_ready():
    """Logs in console when successfully connected to Twitch"""
    # ipdb.set_trace()
    print(f"{BOT_NICK} is online!")


@bot.event
async def event_message(ctx):
    """Passes data to commands when a message is sent to chat
    and greets users if they send a greeting from a list"""
    # stops bot from reacting to itself
    if ctx.author.name.lower() == BOT_NICK.lower():
        return

    # passes message data to command callbacks
    await bot.handle_commands(ctx)

    ipdb.set_trace()

    # greets user if they send a greeting from a list (defined in function)
    await greet(ctx)


# commands, which call functions defined in lib - after adding a new
# function file, be sure to import the file in functions.py
@bot.command(name="count")
async def on_count(ctx):
    """Responds with current count"""
    await count(ctx, JSON_FILEPATH)


@bot.command(name="add")
async def on_add(ctx):
    """Adds to count and responds with new count"""
    await add(ctx, JSON_FILEPATH)


@bot.command(name="sub")
async def on_sub(ctx):
    """Subtracts from count and responds with new counts"""
    await sub(ctx, JSON_FILEPATH)


@bot.command(name="tundexasked")
async def on_tundexasked(ctx):
    """Sets the date when Tundex last asked and responds with confirmation"""
    await tundexasked(ctx, JSON_FILEPATH)


@bot.command(name="dayssincetundexasked")
async def on_dayssincetundexasked(ctx):
    """Responds with the days since Tundex last asked"""
    await dayssincetundexasked(ctx, JSON_FILEPATH)


@bot.command(name="whendidtundexask")
async def on_whendidtundexask(ctx):
    """Responds with the date Tundex last asked"""
    await whendidtundexask(ctx, JSON_FILEPATH)


# launch bot
if __name__ == "__main__":
    bot.run()
