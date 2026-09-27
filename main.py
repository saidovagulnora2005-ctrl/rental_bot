from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from connection import init_table
from dotenv import load_dotenv
from keyboard import main_btn
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

async def main():
    await init_table()
    await dp.start_polling(bot)


if __name__ == "main":
    asyncio.run(main())