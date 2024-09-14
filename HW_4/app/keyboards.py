from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
#Start Buttons
start_buttons = [
    [KeyboardButton(text='Geeks'), KeyboardButton(text='Направления')]
]
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, keyboard=start_buttons)

#Info about geeks websites
geels_inline_b = [
    [InlineKeyboardButton(text='Geeks Pro', url='https://geeks.kg/geeks-pro')],
    [InlineKeyboardButton(text='Основной сайт', url='https://geeks.kg/')],
    [InlineKeyboardButton(text='Geeks Studio', url='https://geekstudio.kg/')]
]
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geels_inline_b)

#Info about geeks directions
dir_inl_b = [
    [InlineKeyboardButton(text='Backend', callback_data='Backend')],
    [InlineKeyboardButton(text='Frontend', callback_data='Frontend')],
    [InlineKeyboardButton(text='Android', callback_data='Android')],
    [InlineKeyboardButton(text='UX/UI', callback_data='UX/UI')]
]
direction_inl_keyboard = InlineKeyboardMarkup(inline_keyboard=dir_inl_b)

#Directions about backend
backend_b = [
    [InlineKeyboardButton(text='Aiogram', callback_data='Aiogram')],
    [InlineKeyboardButton(text='Django', callback_data='Django')],
    [InlineKeyboardButton(text='Python', callback_data='Python')],
]
backend_keyboard = InlineKeyboardMarkup(inline_keyboard=backend_b)

#Directions about frontend
frontend_b = [
    [InlineKeyboardButton(text='HTML', callback_data='HTML')],
    [InlineKeyboardButton(text='CSS', callback_data='CSS')],
    [InlineKeyboardButton(text='JS', callback_data='JS')],
]
frontend_keyboard = InlineKeyboardMarkup(inline_keyboard=frontend_b)

#Directions about android
android_b = [
    [InlineKeyboardButton(text='Нативная разработка', callback_data='Нативная')],
    [InlineKeyboardButton(text='Кроссплатформенная разработка', callback_data='Кроссплатформенная')],
    [InlineKeyboardButton(text='Игровая разработка', callback_data='Игровая')],
]
android_keyboard = InlineKeyboardMarkup(inline_keyboard=android_b)

#Directions about uxui
ux_ui = [
    [InlineKeyboardButton(text='User Experience', callback_data='Experience')],
    [InlineKeyboardButton(text='User Interface', callback_data='Interface')],
]
ux_ui_keyboard = InlineKeyboardMarkup(inline_keyboard=ux_ui)

