from aiogram.types import Message, CallbackQuery  # Типы для сообщений и callback'ов (нажатий на инлайн-кнопки)
from aiogram.filters import Command, CommandStart  # Фильтры для обработки команд /start и других
from aiogram import F, Router  # F — для фильтрации сообщений, Router — для маршрутизации

from lesson_4.app.keyboards import *  # Импортируем клавиатуры, которые были созданы отдельно

# Создаем экземпляр Router, который отвечает за маршрутизацию всех событий
router = Router()

# Обработчик команды /start, которая вызывается, когда пользователь впервые запускает бота
@router.message(CommandStart())
async def start_bot(message: Message):
    """
    Функция вызывается при запуске команды /start.
    Она приветствует пользователя и отображает стартовую клавиатуру.
    """
    await message.reply("Привет", reply_markup=start_keyboard)  # Отправляем приветственное сообщение с клавиатурой

# Обработчик сообщений с текстом "Geeks", например, когда пользователь выбирает эту опцию
@router.message(F.text == "Geeks")
async def greeting(message: Message):
    """
    Функция вызывается, когда пользователь отправляет сообщение с текстом "Geeks".
    Она отправляет информацию о "Geeks" и отображает соответствующую клавиатуру.
    """
    await message.reply("Информация про Geeks", reply_markup=geeks_keyboard)  # Отправляем информацию и клавиатуру

# Обработчик сообщений с текстом "Направления"
@router.message(F.text == "Направления")
async def dir(message: Message):
    """
    Функция вызывается, когда пользователь отправляет сообщение с текстом "Направления".
    Она показывает основные направления и соответствующую клавиатуру.
    """
    await message.reply("Наши основные направления:", reply_markup=direction_keyboard)  # Показываем направления и клавиатуру

# Обработчик инлайн-кнопки с данными 'front', которая вызывается при нажатии на кнопку "Frontend"
@router.callback_query(F.data == 'front')
async def inline_front(callback: CallbackQuery):
    """
    Функция вызывается, когда пользователь нажимает инлайн-кнопку 'Frontend'.
    Она отправляет подтверждение и изменяет текст сообщения, добавляя клавиатуру с разделами Frontend.
    """
    await callback.answer("Вы выбрали направление Frontend")  # Отвечаем на нажатие кнопки
    await callback.message.edit_text("Frontend", reply_markup=front_keyboard)  # Изменяем текст сообщения и добавляем клавиатуру

# Обработчик инлайн-кнопки с данными 'students', которая вызывается при нажатии на кнопку "Наши студенты"
@router.callback_query(F.data == 'students')
async def inline_students_handler(callback: CallbackQuery):
    """
    Функция вызывается, когда пользователь нажимает инлайн-кнопку 'Наши студенты'.
    Она отправляет информацию о студентах с динамически сгенерированной клавиатурой.
    """
    await callback.message.edit_text("Наши студенты", reply_markup=await inline_students())  # Изменяем текст сообщения и показываем студентов

# Эхо-обработчик, который срабатывает, если никакие другие обработчики не сработали (например, на неизвестные сообщения)
@router.message()
async def echo(message: Message):
    """
    Функция эхо-обработчика. Если никакие другие обработчики не сработали,
    бот просто повторяет текст сообщения пользователя.
    """
    await message.answer(message.text)  # Повторяем текст сообщения обратно пользователю
