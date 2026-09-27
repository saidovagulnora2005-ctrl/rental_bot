from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


main_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "🗃️ Каталог"),
            KeyboardButton(text = "📦 Мой инвентарь"),
        ],
    ],
    resize_keyboard = True
)