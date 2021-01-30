import io
import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import AdminFilter, IsGroup
from loader import dp, bot

#zmiana photo
@dp.message_handler(IsGroup(), Command("set_photo"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await bot.set_chat_photo(message.chat.id, photo=input_file)

#zmiana title
@dp.message_handler(IsGroup(), Command("set_title"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title)

#zmiana descriptoin
@dp.message_handler(IsGroup(), Command("set_description"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    await bot.set_chat_description(message.chat.id, description=description)
