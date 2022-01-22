import json

from .helpers.arguments import get_arguments


async def count(ctx, json_filepath):
    count = get_count(json_filepath)
    await ctx.send(f"Current count: {count}")


async def add(ctx, json_filepath):
    command_string = get_arguments(ctx)
    value = None

    try:
        value = int(command_string)
    except ValueError:
        await ctx.send("Incorrect number format. Syntax: !add <integer>")

    if value or value == 0:
        current_count = get_count(json_filepath)
        new_count = current_count + value
        update_count(new_count, json_filepath)
        await ctx.send(f"Added {value} to count. New count: {new_count}")


async def sub(ctx, json_filepath):
    command_string = get_arguments(ctx)
    value = None

    try:
        value = int(command_string)
    except ValueError:
        await ctx.send("Incorrect number format. Syntax: !sub <integer>")

    if value or value == 0:
        current_count = get_count(json_filepath)
        new_count = current_count - value
        update_count(new_count, json_filepath)
        await ctx.send(f"Subtracted {value} from count. New count: {new_count}")


# helpers
def get_count(json_filepath):
    """Reads the count from the JSON file and returns it"""
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        return data["count"]


def update_count(new_count, json_filepath):
    """Updates the JSON file with the new count"""
    data = None

    with open(json_filepath) as json_file:
        data = json.load(json_file)

    if data is not None:
        data["count"] = new_count

    with open(json_filepath, "w") as json_file:
        json.dump(data, json_file, sort_keys=True, indent=4)
