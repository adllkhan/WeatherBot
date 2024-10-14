from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from services import Services
from states import ReqState


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("/weather\nдля получения инфы о погоде")


@router.message(Command("weather"))
async def weather(message: Message, state: FSMContext):
    await state.set_state(ReqState.city)
    await message.answer("Введите город")


@router.message(ReqState.city)
async def handle_city(message: Message, state: FSMContext):
    data = await state.update_data(city=message.text)
    await state.clear()
    info = await Services().get_weather(city=data["city"])
    await message.answer(info)
