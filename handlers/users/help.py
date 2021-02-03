import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit

""" #odpowiedż do komandy help """


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Command list: ',
        '/set_photo - Set the photo in the chat',
        '/set_title - Set the chat name',
        '/set_description - Set the description of the chat',
        '/ro - Enable Read Only mode',
        '/unro - Disable Read Only mode',
        '/ban - Ban user',
        '/unban - Unban user',
        '/help - Command list',
        '/riddles - Answer our riddles',
        '/products - products',
        '/gallery - This is a gallery',
        '/show_on_map - Place for eating',
        '/callback - We will call you'
    ]
    logging.info("dsdsdds")
    await message.answer('\n'.join(text))
