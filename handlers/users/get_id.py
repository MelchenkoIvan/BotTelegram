from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

# get id photo
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id_p(message: types.Message):
#   await message.reply(message.photo[-1].file_id)

# get id video
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def get_file_id_v(message: types.Message):
#   await message.reply(message.video.file_id)
