from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Gallery = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="get_cat")
        ],
        [
            KeyboardButton(text="more_cats")
        ],
    ],
    resize_keyboard=True
)
