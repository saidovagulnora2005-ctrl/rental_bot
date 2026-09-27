from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from connection import init_table
from dotenv import load_dotenv
from keyboard import main_btn
from services import *
import asyncio
import os

load_dotenv()

bot = Bot(os.getenv("API_KEY"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Привет дорогой/дорогая {message.from_user.username}!\n" 
        "Я ваш Бот Прокат Спортивного Инвентаря 🏀🥅⛸️🤿\n"
        "Как я могу вам помочь?",reply_markup=main_btn)


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("📖 Help Menu:\n\n"
        "/add_item - Добавить вещь в каталог\n"
        "Пример: /add_item Футбольный мяч\n\n"
        "/items - Показать свободные вещи\n\n"
        "/rent - Взять вещь на 7 дней\n"
        "Пример: /rent 1\n\n"
        "/return_item - Вернуть вещь\n"
        "Пример: /return_item 1\n\n"
        "/my_rentals - Показать мои аренды")



@dp.message(Command("add_item"))
async def add_item_handler(message: Message):
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer(
            "📝 Чтобы добавить вещь, напиши:\n\n"
            "/add_item Название вещи\n\n"
            "Например:\n"
            "/add_item Футбольный мяч ⚽")
    name = " ".join(parts[1:])
    await add_item(name)
    await message.answer(
        f"✅ {name} добавлен в каталог!")


@dp.message(Command("items"))
async def items_handler(message: Message):
    items = await show_items()
    if items:
        text = "🏀🤿🛹 Свободные вещи:\n\n"
        for item in items:
            text += f"{item['item_id']} - {item['name']}\n"
        text += "\n📌 Чтобы взять вещь в аренду пишем так:\n/rent ID"
    else:
        text = "❌ Сейчас свободных вещей нет."
    await message.answer(text)


async def main():
    await init_table()
    await dp.start_polling(bot)


if __name__ == "main":
    asyncio.run(main())