import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp


@dp.message_handler(Command("products"))
# wywoływanie InlineKeyboardMarkup from chpice_buttons
async def show_items(message: Message):
    await message.answer(text="What you want?", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    # Pamiętaj, aby natychmiast udzielić odpowiedzi, aby usunąć „zegarek” po naciśnięciu przycisku.
    # Określ cache_time, aby bot nie otrzymywał aktualizacji przez jakiś czas, wtedy poniższy kod nie zostanie wykonany.
    await call.answer(cache_time=60)

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Pear? Are you sure? We have {quantity} pears ",
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apple(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Apple? Are you sure? We have {quantity} apples ",reply_markup=apples_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Odpowiemy w okienku powiadomienia!
    await call.answer("You canceled this purchasew!", show_alert=True)

    # Wysyłamy pustą klawiaturę, zmieniając wiadomość, aby usunąć ją z wiadomości!
    await call.message.edit_reply_markup(reply_markup=None)
