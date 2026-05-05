import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from database import add_player, init_db

# Инициализация бота (токен будем брать из env)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем базу при запуске
init_db()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в Crypto Syndicate! Используй /join, чтобы войти в игру.")

@dp.message(Command("join"))
async def cmd_join(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or f"user_{user_id}"
    add_player(user_id, username)
    await message.answer(f"Ты в игре, {username}! Твой стартовый капитал: 1000 $SYNC.")
