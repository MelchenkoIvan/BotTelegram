from aiogram.dispatcher.filters import Command, Text

from keyboards.default import Gallery

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ReplyKeyboardRemove

from loader import dp, bot


@dp.message_handler(Command("Gallery"))
async def show_menu(message: types.Message):
    await message.answer("Welcome to gallery", reply_markup=Gallery)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    """cat id"""

    photo = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"
    """ wysyłanie zdjęcia na czat """

    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption="This is a cat /more_cats", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    """ tworzenie albumu """

    album = types.MediaGroup()

    """ Dołączanie zdjęć i filmów """

    photo_file_id = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"
    photo_bytes = InputFile("photos/cat.jpg")
    video_file_id = "BAACAgQAAx0CVnNxwgACARZf-xLc9nx9hGf7pjxv-iysq2SU-QAC9QoAAjYM2VNWhQ005RkYAR4E"
    album.attach_photo(
        photo=photo_file_id,
        caption="Funny cats")

    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id)

    """ wysyłanie albumu """
    await message.answer_media_group(media=album)
    await message.answer('Thanks for watching', reply_markup=ReplyKeyboardRemove())
