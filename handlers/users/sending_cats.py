from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    photo = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"  # File id
    # photo = "https://www.meme-arsenal.com/memes/3f5777727d3f6e263b4edbee5bd15a1b.jpg" # URL
    # photo = InputFile(path_or_bytesio="photos/cat.jpg")  # Local file
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption="This is a cat /more_cats")


@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    # Создаем альбом
    album = types.MediaGroup()

    # Прикрепляем фото и видео
    photo_file_id = "AgACAgQAAx0CVnNxwgACARRf-xIjGEjWVvKuv8zGjEnxk-E38wACHqoxG7Zg3FNMdd3_v0xcuVgVqhsABAEAAwIAA3cAAxvLAQABHgQ"
    photo_bytes = InputFile("photos/cat.jpg")
    video_file_id = "BAACAgQAAx0CVnNxwgACARZf-xLc9nx9hGf7pjxv-iysq2SU-QAC9QoAAjYM2VNWhQ005RkYAR4E"
    album.attach_photo(
        photo=photo_file_id,
        caption="Прикольный котик")

    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id,
                       caption="M")

    # Отправляем
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)