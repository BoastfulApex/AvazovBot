from aiogram.dispatcher.filters.state import State, StatesGroup


class UserForm(StatesGroup):
    name = State()
    test1 = State()
    test2 = State()
    test3 = State()
    test4 = State()
    test5 = State()
    sog = State()
    phone_number = State()


users = {}
