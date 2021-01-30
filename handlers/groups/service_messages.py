import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot

#reakcja bota jeżeli dodany nowy user do czatu
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Hi,{members}.")

#reakcja bota jeżeli user usuninty lub wyszedł z czatu
@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} left the chat")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} was removed from chat."
                             f"The user who deleted him{message.from_user.get_mention(as_html=True)}.")



