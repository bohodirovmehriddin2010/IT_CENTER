from aiogram.dispatcher.filters.state import State, StatesGroup


class aplication(StatesGroup):
    phone = State()
    age = State()
    check = State()
    name = State()
    course = State()