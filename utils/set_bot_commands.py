from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Command list"),
        types.BotCommand("gallery", "This is a gallery"),
        types.BotCommand("riddles", "Answer our riddles"),
        types.BotCommand("show_on_map", "Place for eating"),
        types.BotCommand("set_photo", "Set the photo in the chat"),
        types.BotCommand("set_title", "Set the chat name"),
        types.BotCommand("set_description", "Set the description of the chat"),
        types.BotCommand("ro", "Enable Read Only mode"),
        types.BotCommand("unro", "Disable Read Only mode"),
        types.BotCommand("ban", "Ban user"),
        types.BotCommand("unban", "Unban user"),
        types.BotCommand("products", "products"),
        types.BotCommand("callback", "We will call you")
    ])
