from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import location_button
from utils.misc.calc_distance import choose_shortest
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot


@dp.message_handler(Command("show_on_map"))
async def share_number(message: types.Message):
    """ prosimy usera o lokacji"""

    await message.answer(f"Hi, {message.from_user.full_name}.\n"
                         f"In order to find the nearest KFC, send us your location ")


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: types.Message):
    """ zapisujemy danne """

    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    """ wywoływanie funkcji co wybiera najbliższe sklepy """

    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"Name: {shop_name}. <a href='{url}'>Google</a>\n The distance to the KFS: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])
    """ wysyłanie odpowiedzi """

    await message.answer(f"Thanks. \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
