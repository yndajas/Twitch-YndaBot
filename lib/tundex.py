import datetime
import json

async def tundexasked(ctx, json_filepath):
    # parse command
    command_string = ctx.message.content
    # remove command and white space
    command_string = command_string.replace('!tundexasked', '').strip()

    date = None

    if (len(command_string) > 0):
        try:
            date = datetime.datetime.strptime(command_string, '%Y%m%d')
        except ValueError:
            await ctx.send('Incorrect date format')
    else:
        date = datetime.date.today()

    if (date != None):
        data = None

        with open(json_filepath) as json_file:
            data = json.load(json_file)

        if data is not None:
            data['tundexasked'] = date.strftime('%Y%m%d')

        with open(json_filepath, 'w') as json_file:
            json.dump(data, json_file, sort_keys=True, indent=4)
        
        await ctx.send(f'Tundex asked again!? Taking note that Tundex asked on {date.strftime("%-d %B %Y")}')

async def dayssincetundexasked(ctx, json_filepath):
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        date_string = data['tundexasked']
        date = datetime.datetime.strptime(date_string, '%Y%m%d')
        days_since_date = datetime.datetime.today() - date
        await ctx.send(f'Tundex last asked {days_since_date.days} days ago')

async def whendidtundexask(ctx, json_filepath):
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        date_string = data['tundexasked']
        date = datetime.datetime.strptime(date_string, '%Y%m%d')
        await ctx.send(f'Tundex last asked on {date.strftime("%-d %B %Y")}')