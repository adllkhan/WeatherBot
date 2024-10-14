from aiogram.fsm.state import State, StatesGroup


class ReqState(StatesGroup):
    city = State()
