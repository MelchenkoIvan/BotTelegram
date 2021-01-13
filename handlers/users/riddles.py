from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("riddles"))
async def enter_test(message: types.Message):
    await message.answer("The test is started.\n"
                         "What can fill a room but takes up no space ?")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("Question 2.\n"
                         "If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    data = await  state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    correct_answer1 = "Light"
    correct_answer2 = "Mirror"
    await message.answer("Thanks for your answer")
    await message.answer(f"Answer 1: {answer1}. Correct answer: {correct_answer1}")
    await message.answer(f"Answer 2: {answer2}. Correct answer: {correct_answer2}")

    await state.reset_state()
