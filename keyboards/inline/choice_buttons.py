from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kupić pear",
                                 callback_data=buy_callback.new(item_name="pear",
                                                                quantity=1)),
            InlineKeyboardButton(text="kupić apple", callback_data="buy:apple:5")
        ],
        [
            InlineKeyboardButton(text="anulowanie", callback_data="cancel")
        ]
    ])
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Buy here", url="https://rozetka.com.ua/champion_a00225/p27223057")
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Buy here", url="https://freshmart.com.ua/product/yabloko-gala-116.html")
    ]
])
