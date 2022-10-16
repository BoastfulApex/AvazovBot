from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


async def get_number():
    btn = KeyboardButton('Raqamni yuborish 📞', request_contact=True)
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(btn)
    return markup

async def go_info():
    btn = KeyboardButton('Ro\'yxatdan o\'tish ▶️')
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(btn)
    return markup
