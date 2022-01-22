import inspect


def get_arguments(ctx):
    function_name = inspect.stack()[1].function
    return ctx.message.content.replace(f"!{function_name}", "").strip()
