from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder  # Утилита для создания инлайн-клавиатур

# Стартовая клавиатура с двумя основными кнопками
start_button = [
    [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")]  # Обычные кнопки, выполняют команды
]
# ReplyKeyboardMarkup — обычная клавиатура с текстовыми кнопками
start_keyboard = ReplyKeyboardMarkup(
    keyboard=start_button,
    resize_keyboard=True,  # Клавиатура подгоняется под экран пользователя
    one_time_keyboard=True,  # Клавиатура исчезает после использования
    input_field_placeholder="Текст-подсказка для ввода"  # Текст-подсказка в поле ввода
)

# Инлайн-клавиатура для выбора направлений
direction_inline = [
    [InlineKeyboardButton(text="Кнопка для URL 1", url="URL"),
     InlineKeyboardButton(text="Кнопка для Callback 1", callback_data='callback_data_1')]  # Инлайн-кнопка с callback
]
# InlineKeyboardMarkup — клавиатура, встроенная в сообщение (инлайн)
direction_keyboard = InlineKeyboardMarkup(inline_keyboard=direction_inline)

# Инлайн-клавиатура с тремя кнопками для другого направления
front_inline = [
    [InlineKeyboardButton(text="Кнопка для URL 2", url="URL")],  # Кнопка с ссылкой (URL)
    [InlineKeyboardButton(text="Кнопка для URL 3", url="URL")],
    [InlineKeyboardButton(text="Кнопка для URL 4", url="URL")]
]
# Инлайн-клавиатура для второго направления (например, Frontend)
front_keyboard = InlineKeyboardMarkup(inline_keyboard=front_inline)

# Инлайн-клавиатура для дополнительной информации (например, о студентах и менторах)
geeks_inline = [
    [InlineKeyboardButton(text="Кнопка для Callback 2", callback_data="callback_data_2")],  # Кнопка с callback для студентов
    [InlineKeyboardButton(text="Кнопка для Callback 3", callback_data="callback_data_3")],  # Кнопка с callback для менторов
]
# Инлайн-клавиатура для информации о студентах и менторах
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)

# Список динамических значений для генерации инлайн-клавиатуры (например, список студентов)
students = ["Имя студента 1", "Имя студента 2", "Имя студента 3"]  # Список студентов

# Асинхронная функция для создания инлайн-клавиатуры с динамическими данными
async def inline_students():
    keyboard = InlineKeyboardBuilder()  # Создаем объект для динамического построения клавиатуры
    for student in students:
        # Добавляем кнопку для каждого элемента (например, для каждого студента)
        keyboard.add(InlineKeyboardButton(text=student, url="URL"))  # Кнопка с динамическим текстом и URL
    return keyboard.adjust(1).as_markup()  # Возвращаем инлайн-клавиатуру с одной колонкой
