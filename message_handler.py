from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_token import bot, dp
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from buttons import get_number
import re

def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


@dp.message_handler(state="go_info", content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == "Ro\'yxatdan o\'tish ▶️":
        await message.answer(text="Iltimos Ismnimgizni kiriting ✍️", reply_markup=ReplyKeyboardRemove())
        await state.set_state("get_name")

@dp.message_handler(state="get_name", content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    markup = await get_number()
    await message.answer(text="Telefon raqamingizni yuboring yoki 9989YXXXXXXX kabi formatda kiriting 👇", reply_markup=markup)
    await state.set_state("get_phone")
    
@dp.message_handler(state="get_phone", content_types=types.ContentTypes.CONTACT)
async def get_name(message: types.Message, state: FSMContext):
    if message.contact:
        await state.update_data(contact=message.contact)
        await message.answer("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi✅", reply_markup=ReplyKeyboardRemove())
        file = open("./file.pdf", "rb")
        await bot.send_document(chat_id=message.from_user.id, document=file)
        await state.finish()


@dp.message_handler(state="get_phone", content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    if message.text:
        if isValid(message.text):
            await message.answer("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi✅", reply_markup=ReplyKeyboardRemove())
            file = open("./file.pdf", "rb")
            await bot.send_document(chat_id=message.from_user.id, document=file)
            await state.finish()
        else:
            markup = await get_number()
            await message.answer(text="Telefon raqam noto'g'ri formatda kiritildi⚠️ \nTelefon raqamingizni yuboring yoki 9989YXXXXXXX kabi formatda kiriting 👇", reply_markup=markup)
            await state.set_state("get_phone")


@dp.message_handler(state="get_state", content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    shtat = message.text
    data = await state.get_data()
    name = data['name']
    contact = data['contact']
    text = f"<b>Ismi</b>: {name}\n\n<b>Telefon</b>: {contact}\n\n<b>Shtat</b>: {shtat}"
    await bot.send_message(chat_id=-675610884, text=text)
    await message.answer("Rahmat! Tez orada siz bilan aloqaga chiqamiz", parse_mode="HTML")
    await state.finish()
    
