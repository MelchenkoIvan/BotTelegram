import logging

from aiogram import Dispatcher

from data.config import admins


async def mail_to_admins(dp):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Bot is ready!")

        except Exception as err:
            logging.exception(err)


async def on_startup_notify(dp: Dispatcher):
    await mail_to_admins(dp)