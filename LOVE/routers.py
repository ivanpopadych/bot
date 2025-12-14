from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
import random, os


class LoveState(StatesGroup):
    answer1 = State()
    answer2 = State()
    answer3 = State()
    answer4 = State()
    answer5 = State()


    


async def false_answer(message: Message):
    photos_dir = os.path.join(os.path.dirname(__file__), "photos")
    try:
        files = [f for f in os.listdir(photos_dir) if os.path.isfile(os.path.join(photos_dir, f))]
        if not files:
            await message.answer("Думай киця думай краще)")
            return
        random_photo = random.choice(files)
        photo_path = os.path.join(photos_dir, random_photo)
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo, caption="Думай киця думай краще)")
    except Exception:
        await message.answer("Помилка надсилання фото, спробуй ще раз.")


router = Router()




answers = {
    1: "19",
    2: "15",
    3: "69",
    4: "8",
    5: "317.2"
}

@router.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    await message.answer("2x+5 = 15\n4y+11 = x")
    await message.answer("y = ?")
    await state.set_state(LoveState.answer1)



@router.message(F.text, LoveState.answer1)
async def answer_1(message: Message, state: FSMContext):
    if message.text == answers[1]:
        await message.answer("x^2 - 14x-15 = 0")
        await message.answer("x = ?")
        await state.set_state(LoveState.answer2)
    else:
        await false_answer(message)

@router.message(F.text, LoveState.answer2)
async def answer_2(message: Message, state: FSMContext):
    if message.text == answers[2]:
        await message.answer("11^3/11 - √400-32=")
        await state.set_state(LoveState.answer3)
    else:
        await false_answer(message)
@router.message(F.text, LoveState.answer3)
async def answer_3(message: Message, state: FSMContext):
    if message.text == answers[3]:
        await message.answer("2+2 = ?")
        await state.set_state(LoveState.answer4)
    else:
        await false_answer(message)

@router.message(F.text, LoveState.answer4)
async def answer_4(message: Message, state: FSMContext):
    if message.text == answers[4]:
        await message.answer("100*(1/2+3.172)-50 = ")
        await state.set_state(LoveState.answer5)
    else:
        await false_answer(message)
@router.message(F.text, LoveState.answer5)
async def answer_5(message: Message, state: FSMContext):
    if message.text == answers[5]:
        await message.answer("Умнічка ❤️‍🔥")
        await message.answer("Подивись на останню відповідь!")
        await state.clear()
    else:
        await false_answer(message)


