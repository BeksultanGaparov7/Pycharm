import asyncio
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
import aiogram

from Closed_files.config import token


bot = Bot(token=token)
dp = Dispatcher()



buttons = [
    [KeyboardButton(text='График работы'), KeyboardButton(text="О нас")]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply(f"Привет {message.from_user.id}", reply_markup=keyboard)

@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Помогу чем смогу /start")


@dp.message(F.text == "График работы")
async def greeting(message: Message):
    await message.reply("09:00 - 21:00")


@dp.message(F.text == "О нас")
async def about_us(message: Message):
    await message.answer("НАША МИССИЯ МЫ СОЗДАЕМ ЭКОСИСТЕМУ ДЛЯ ОБУЧЕНИЯ,  РАБОТЫ И ТВОРЧЕСТВА IT-СПЕЦИАЛИСТОВ")
    await message.answer('ИСТОРИЯ СОЗДАНИЯ')
    await message.answer('Международная IT-академия Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию.')
    await message.answer_photo('https://geeks.kg/back_media/general/2023/06/22/Rectangle_1409_7rACGFN.webp')

@dp.message(F.text == "Как дела?")
async def greeting(message: Message):
    await message.reply("Хорошо")


@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")

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