from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from bot_token import dp
from aiogram.dispatcher import FSMContext
from buttons import go_info


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    markup = await go_info()
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}👋.\nAlisher Avazovning rasmiy botiga xush kelibsiz. Bepul konsultatsiya olish uchun ro'yxatdan o'ting 👇.", reply_markup=markup)
    await state.set_state("go_info")
