from aiogram.dispatcher.filters import Command, Text

from keyboards.default import Gallery

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ReplyKeyboardRemove

from loader import dp, bot


@dp.message_handler(Command("Gallery"))
async def show_menu(message: types.Message):
    await message.answer("Welcome to gallery", reply_markup=Gallery)


@dp.message_handler(text="get_cat")
async def send_cat(message: types.Message):
    photo = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"  # File id
    # photo = "https://www.meme-arsenal.com/memes/3f5777727d3f6e263b4edbee5bd15a1b.jpg" # URL
    # photo = InputFile(path_or_bytesio="photos/cat.jpg")  # Local file
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption="This is a cat /more_cats", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="more_cats")
async def more_cats(message: types.Message):
    # Создаем альбом
    album = types.MediaGroup()

    # Прикрепляем фото и видео
    photo_file_id = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"
    photo_bytes = InputFile("photos/cat.jpg")
    video_file_id = "BAACAgQAAx0CVnNxwgACARZf-xLc9nx9hGf7pjxv-iysq2SU-QAC9QoAAjYM2VNWhQ005RkYAR4E"
    album.attach_photo(
        photo=photo_file_id,
        caption="Funny cat")

    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id)

    # Отправляем
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
