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


async def main():
    await init_table()
    await dp.start_polling(bot)


if __name__ == "main":
    asyncio.run(main())