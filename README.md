# Twitch YndaBot

Custom Twitch chat bot with various commands

 ## Setup

*Adapted from [How to make your own Custom Twitch Chat Bot for Free | (incl. Download)](https://youtu.be/CPVSoowZhVw)*

Note: in order to run the bot locally, you'll need to install Python 3

### Twitch account and auth codes

1. Create a new Twitch account for your bot
2. Get an OAuth code from [twitchapps.com/tmi](https://twitchapps.com/tmi) - it'll look like 'oauth:' then a bunch of letters and numbers
3. Go to the `Twitch Developers Console` and create a new app
  a. Under "Name", you can probably put anything, but it makes sense to provide the username of your bot account
  b. Under "OAuth Redirect URLs", enter something like "https://localhost"
  c. Under "Category", select "Chat Bot"
  d. Click on "Create", then "Manage" in the next page and make note of the client ID

### Code setup

1. Clone the repository
2. In a terminal, navigate into the repository's directory and enter `pip3 install -r requirements.txt`
3. Create a copy of ".env.sample" and add your information:
  a. After `TMI_TOKEN=`, enter the OAuth code from step two in the previous section
  b. After `CLIENT_ID=`, enter the client ID from step three in the previous section
  c. After `BOT_NICK=`, enter your bot's username
  d. You can leave `BOT_PREFIX=!` unchanged unless you want a different command prefix
  e. After `CHANNEL=`, enter the channel you want the bot to work on

## Running the bot

After following the setup instructions and ensuring Python 3 is installed, from a terminal, enter `python3 bot.py`

Assuming everything is working, it will say `<bot name> is online!`

## Functionality

### Commandless

**Greeting:** if a greeting from the list in [lib/greety.py](./lib/greet.py) is sent without tagging anyone, the bot will respond

### Commands
#### Count

`!count` respond with current count
`!add <integer>` add the given integer to the count and respond with new count
`!sub <integer>` subtractthe given integer to the count and respond with new count

#### Tundex

`!tundexasked` record that someone called Tundex asked something again today and respond with confirmation
`!tundexasked <date in format yyyymmdd>` record that someone called Tundex last asked something on the given date and respond with confirmation
`!dayssincetundexasked` respond with the number of days since this Tundex person asked something
`!whendidtundexask` respond with the date this Tundex person last asked something

## Adding commands

To add a command, there are a few steps. For example, if you wanted to add a command that responded "GOAT" to `!outkast`, you would need to:
1. In [bot.py](./bot.py), before the line `if __name__ == "__main__":`, enter:
```
@bot.command(name="outkast")
async def on_outkast(ctx):
    """An optional description of the command"""
    await outkast(ctx)
```
2. Add a file called "outkast.py" to [lib](./lib) - the name doesn't actually matter, as long as you reference it properly, but you should provide a sensible name. In the file, add the following:
```
async def outkast(ctx):
    await ctx.send("GOAT")
```
3. In [functions.py](./functions.py), add `from lib.outkast import *` (or from `lib.outkast import outkast`)

Note: this is a simple command that responds the same way every time. You could also make it respond to words added after the command in the user's message, and read and/or write to stored data. The existing commands provide examples of how to implement such functionality (all of them read/write data, and some of them parse words added after the command). Commands could also respond differently to different authors, or to authors who are mods versus authors who aren't. Examples of this functionality is not yet provided.

## Credits

Developed on top of the foundations of [k0nze](https://github.com/k0nze)'s [Twitch Count Bot](https://github.com/k0nze/twitch_count_bot), with guidance from their YouTube guide referenced in the setup section. Their bot is similar to [NinjaBunny9000](https://github.com/NinjaBunny9000)'s [Barebones Twitch Bot](https://github.com/NinjaBunny9000/barebones-twitch-bot), which has a companion [guide article](https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8). Twitch Count Bot, Barebones Twitch Bot and YndaBot utilise [TwitchIO](https://github.com/TwitchIO/TwitchIO), a Python wrapper around the Twitch API.  