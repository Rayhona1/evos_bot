from loader import dp
from aiogram.types import Message
from keyboards.reply_btn import start_command_btn, settings_btn

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    btn = await start_command_btn()
    await message.answer(f'Salom', reply_markup=btn)

@dp.message_handler(text='⚙️ Настройки')
async def settings_command(message: Message):
    btn = await settings_btn()
    await message.answer(f'Выберите действие:', reply_markup=btn)

@dp.message_handler(text="⬅️ Назад")
async def back_handler(message: Message):
    btn = await start_command_btn()  # Re-create the start command button
    await message.answer(f'Выберите действие:', reply_markup=btn)
