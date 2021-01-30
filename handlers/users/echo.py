from aiogram import types
from loader import dp

# odpowiada tym samym co napisałeś
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
