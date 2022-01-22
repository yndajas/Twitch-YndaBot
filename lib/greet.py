async def greet(ctx):
    greetings = [
        "Ahn nyong ha se yo",
        "Ahn-nyong-ha-se-yo",
        "Ahoj",
        "An-nyŏng-ha-se-yo",
        "As-salamu alaykum",
        "Assalamo aleikum",
        "Assalamualaikum",
        "Avuxeni",
        "Bonġu",
        "Bonjour",
        "Bună ziua",
        "Ciao",
        "Cześć",
        "Dia dhuit",
        "Dobar dan",
        "Dobra većer",
        "Dobro jutro",
        "God dag",
        "Góðan dag",
        "Grüß gott",
        "Guten tag",
        "Hafa adai",
        "Hallå",
        "Hallo",
        "Hello",
        "Hoi",
        "Hola",
        "How ya doing",
        "How you doing",
        "Howdy",
        "Hujambo",
        "Hyvää päivää",
        "Ia orna",
        "Jo napot",
        "Konnichiwa",
        "Marhaba",
        "Merhaba",
        "Moïen",
        "Namaskar",
        "Namaste",
        "Namastē",
        "Nde-ewo",
        "Nǐ hǎo",
        "Niltze",
        "Now then",
        "Olá",
        "Salam",
        "Salve",
        "Sawasdee",
        "Sawubona",
        "Selamat siang",
        "Shalom",
        "Shwmae",
        "Sveiki",
        "Wassup",
        "What's up",
        "Xin chào",
        "Yasou",
        "Zdraveite",
        "Zdravo",
        "Zdravstvuyte",
        "안녕하세요",
        "こんにちは",
        "你好",
    ]

    message = ctx.content.lower()

    # if no one is tagged in the message
    if "@" not in message:
        message_greetings = []

        # check if any of the greetings are in the message
        for greeting in greetings:
            if greeting.lower() in message:
                message_greetings.append(greeting)

        # if any are, format them into a greeting back to the user
        if len(message_greetings) > 0:
            greetings_string = message_greetings[0]

            if len(message_greetings) > 1:
                first_greeting = message_greetings[0]
                other_greetings = []

                for greeting in message_greetings[1 : len(message_greetings)]:
                    other_greetings.append(greeting.lower())

                all_greetings = [first_greeting] + other_greetings

                if len(message_greetings) > 2:
                    greetings_string = (
                        f"{', '.join(all_greetings[0:-1])} and {all_greetings[-1]}"
                    )
                else:
                    greetings_string = " and ".join(all_greetings)

            # respond to user
            await ctx.channel.send(f"{greetings_string}, @{ctx.author.name}!")
