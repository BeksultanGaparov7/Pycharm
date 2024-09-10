import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import aiogram

from Closed_files.config import token

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

# Connect to SQLite database
connect = sqlite3.connect('Closed_files/tasks.db')
cursor = connect.cursor()

# Create tasks table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INT,
        task TEXT
    )
''')
connect.commit()

# Global dictionary to store users' task deletion state
delete_state = {}

# Start command handler
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}, я бот 🤖 для управления твоими задачами.')
    await message.answer('Вот список команд: /add ➕, /view 👀, /delete 🗑')

# Add task command handler
@dp.message(Command('add'))
async def add(message: Message):
    logging.info(f"Received /add from {message.from_user.id}")
    task_text = message.text.replace('/add', '').strip()

    if task_text:
        user_id = message.from_user.id
        cursor.execute('INSERT INTO tasks (user_id, task) VALUES (?, ?)', (user_id, task_text))
        connect.commit()
        await message.answer(f'Задача "{task_text}" добавлена!')
    else:
        await message.answer('Пожалуйста, укажите задачу после команды /add.')

# View tasks command handler
@dp.message(Command('view'))
async def view(message: Message):
    user_id = message.from_user.id
    cursor.execute('SELECT task FROM tasks WHERE user_id = ?', (user_id,))
    data = cursor.fetchall()

    if data:
        tasks = '\n'.join([f'{i+1}. {task[0]}' for i, task in enumerate(data)])  # Numbered tasks
        await message.answer(f'Ваши задачи:\n{tasks}')
    else:
        await message.answer('У вас пока нет задач.')

# Delete task command handler
@dp.message(Command('delete'))
async def delete(message: Message):
    user_id = message.from_user.id
    cursor.execute('SELECT id, task FROM tasks WHERE user_id = ?', (user_id,))
    data = cursor.fetchall()

    if data:
        # Show the tasks with numbers
        tasks = '\n'.join([f'{i+1}. {task[1]}' for i, task in enumerate(data)])
        await message.answer(f'Ваши задачи:\n{tasks}')
        await message.answer('Введите номер задачи, которую хотите удалить:')

        # Save the task IDs to keep track of them when the user responds with a number
        delete_state[user_id] = [task[0] for task in data]
    else:
        await message.answer('У вас нет задач для удаления.')

# Handle the user's response for task deletion
@dp.message()
async def handle_delete_response(message: Message):
    user_id = message.from_user.id

    # Check if the user is in the delete state
    if user_id in delete_state:
        try:
            task_number = int(message.text) - 1  # User enters task number (1-based index)
            if 0 <= task_number < len(delete_state[user_id]):
                task_id = delete_state[user_id][task_number]

                # Delete the task from the database
                cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
                connect.commit()

                await message.answer('Задача удалена!')

                # Clear the delete state for the user
                del delete_state[user_id]
            else:
                await message.answer('Неверный номер задачи. Попробуйте еще раз.')
        except ValueError:
            await message.answer('Введите корректный номер задачи.')
    else:
        # If the user is not in the delete state, ignore or handle other messages
        await message.answer('Введите команду для взаимодействия с ботом.')


# Main polling function
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
