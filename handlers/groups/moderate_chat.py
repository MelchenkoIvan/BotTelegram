import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("ro"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
        await message.answer(f"User {member.get_mention(as_html=True)} is muted for {time} minutes."
                             f"Reason: {comment}")
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Error! {err.args}")
        return

    service_message = await message.reply("The message will be deleted after 10 seconds.")
    await asyncio.sleep(10)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unro"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("The message will be deleted after 10 seconds.")
    # Пауза 5 сек
    await asyncio.sleep(10)

    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"User {member.full_name} is not muted")

    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    await message.chat.kick(user_id=member_id)

    await message.answer(f"User {message.reply_to_message.from_user.full_name} is ban")
    service_message = await message.reply("The message will be deleted after 10 seconds.")

    await asyncio.sleep(10)

    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)

    await message.answer(f"User {message.reply_to_message.from_user.full_name} is unban")
    service_message = await message.reply("The message will be deleted after 10 seconds.")

    await asyncio.sleep(10)

    await message.delete()
    await service_message.delete()
