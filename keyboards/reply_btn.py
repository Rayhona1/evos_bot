from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

async def start_command_btn():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.row(
         KeyboardButton(text='🍴 Меню'),
    )
    btn.row(
        KeyboardButton(text='🛍 Мои заказы'),
 )   
    btn.row(
        KeyboardButton(text='✍️ Оставить отзыв'),
        KeyboardButton(text='⚙️ Настройки'),
 )   
    return btn

async def settings_btn():
    btn = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn.add(
        KeyboardButton(text='Изменить язык'),
        KeyboardButton(text="⬅️ Назад")
    
            )
    return btn