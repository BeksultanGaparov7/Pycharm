import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import aiogram

from Closed_files.config import token

bot = Bot(token=token)
dp = Dispatcher()


connect = sqlite3.connect('Closed_files/users.db')
cursor = connect.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (20),
    surname VARCHAR (20),
    username VARCHAR (30),
    age INT,
    is_premium BOOLEAN
) ''')


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer('Hello')
    username = message.from_user.username
    name = message.from_user.first_name
    surname = message.from_user.last_name
    is_premium = message.from_user.is_premium
    cursor.execute(f'SELECT username FROM users WHERE username = {message.from_user.username}')
    user = cursor.fetchall()
    if user == []:
        cursor.execute('INSERT INTO users(name, surname, username, is_premium) VALUES(?,?,?,?)',
                       (name, surname, username, is_premium))
        connect.commit()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    await message.answer(f'Complete successful {data}')



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
    except aiogram.exceptions.TelegramNetworkError:
        print("Network error occurred.")