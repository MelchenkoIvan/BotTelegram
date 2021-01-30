from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import contact_button

from loader import dp, bot


@dp.message_handler(Command("callback"))
async def share_number(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}.\n"
                         f"Please send your phone number and we will call you"
                         )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    #zapisyłanie contakty
    contact = message.contact
    #wysyłanie odpowiedzi
    await message.answer(f"Thanks, {contact.full_name}.\n"
                         f"Your phone number {contact.phone_number} was get. Please wait.",
                         reply_markup=ReplyKeyboardRemove())
