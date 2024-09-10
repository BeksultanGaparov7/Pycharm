import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import logging
from Closed_files.config import token
from random import randint

bot = Bot(token=token)
dp = Dispatcher()

current_number = None

async def main():
    await dp.start_polling(bot)


def random_int():
    global current_number
    current_number = str(randint(1, 3))
    return current_number

@dp.message(CommandStart())
async def start(message: Message):
    random_int()
    await message.answer('Я загадал число от 1 до 3, угадайте!')

@dp.message(F.text)
async def guess(message: Message):
    if message.text == current_number:
        await message.answer_photo(photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg',
                                   caption='Правильно, вы отгадали!')
        random_int()
    else:
        await message.answer_photo(photo='https://media.makeameme.org/created/sorry-you-lose.jpg',caption='Неправильно, попробуйте еще раз!')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")





