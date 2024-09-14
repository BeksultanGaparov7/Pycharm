from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

from HW_4.app.keyboards import *
from HW_4.app.info import *

router = Router()



@router.message(CommandStart())
async def start(message : Message):
    await message.answer('Привет я бот от Geeks!',reply_markup=start_keyboard)


@router.message(F.text == 'Geeks')
async def Geeks(message : Message):
    await message.answer('Вот сайты от GEEKS: ',reply_markup=geeks_keyboard)


@router.message(F.text == 'Направления')
async def directions(message : Message):
    await message.answer('Вот направления в GEEKS: ', reply_markup=direction_inl_keyboard)

@router.callback_query(F.data == 'Backend')
async def backend(callback : CallbackQuery):
    await callback.message.answer(inf_backend, reply_markup=backend_keyboard)


@router.callback_query(F.data == 'Frontend')
async def frontend(callback : CallbackQuery):
    await callback.message.answer(inf_frontend, reply_markup=frontend_keyboard)

@router.callback_query(F.data == 'Android')
async def android(callback : CallbackQuery):
    await callback.message.answer(inf_android, reply_markup=android_keyboard)

@router.callback_query(F.data == 'UX/UI')
async def ux_ui(callback : CallbackQuery):
    await callback.message.answer(inf_android, reply_markup=ux_ui_keyboard)


@router.callback_query(F.data == 'Aiogram')
async def aiogram(callback : CallbackQuery):
    await callback.answer('Вы выбрали aiogram.')
    await callback.message.answer('**Aiogram** — это библиотека для создания ботов в Telegram на Python. Она предоставляет удобный API для работы с Telegram Bot API, поддерживает асинхронное программирование и упрощает обработку обновлений и сообщений.')

@router.callback_query(F.data == 'Django')
async def django(callback : CallbackQuery):
    await callback.answer('Вы выбрали django.')
    await callback.message.answer('**Django** — это высокоуровневый веб-фреймворк на Python, который упрощает создание мощных и масштабируемых веб-приложений. Он предоставляет встроенные инструменты для работы с базами данных, управления пользователями и создания административных панелей.')

@router.callback_query(F.data == 'Python')
async def python(callback : CallbackQuery):
    await callback.answer('Вы выбрали python.')
    await callback.message.answer('**Python** — это высокоуровневый, интерпретируемый язык программирования, известный своей читаемостью и простотой синтаксиса. Он поддерживает множество парадигм программирования, включая объектно-ориентированное, процедурное и функциональное. Python широко используется в веб-разработке, анализе данных, машинном обучении и автоматизации.')


@router.callback_query(F.data == 'HTML')
async def html(callback : CallbackQuery):
    await callback.answer('Вы выбрали html.')
    await callback.message.answer('**HTML** (HyperText Markup Language) — это стандартный язык разметки для создания веб-страниц. Он используется для структурирования контента в интернете, определяя элементы, такие как заголовки, абзацы, ссылки и изображения, с помощью тегов. HTML формирует основу веб-документов и часто используется вместе с CSS и JavaScript для создания интерактивных и стилизованных веб-страниц.')


@router.callback_query(F.data == 'CSS')
async def css(callback : CallbackQuery):
    await callback.answer('Вы выбрали css.')
    await callback.message.answer('**CSS** (Cascading Style Sheets) — это язык стилей, который используется для описания внешнего вида HTML-документов. CSS позволяет задавать цвета, шрифты, макеты, отступы и другие визуальные аспекты веб-страниц. Он разделяет содержание документа (HTML) и его представление, что упрощает изменение стиля и поддержание единого дизайна на сайте. CSS используется для создания адаптивного и привлекательного дизайна веб-страниц.')


@router.callback_query(F.data == 'JS')
async def js(callback : CallbackQuery):
    await callback.answer('Вы выбрали js.')
    await callback.message.answer('**JavaScript (JS)** — это язык программирования, который позволяет создавать интерактивные элементы на веб-страницах. Он используется для управления динамическим содержимым, обработки событий, выполнения анимаций и взаимодействия с сервером через AJAX. JavaScript делает веб-страницы более функциональными и отзывчивыми, позволяя пользователям взаимодействовать с ними в реальном времени.')


@router.callback_query(F.data == 'Нативная')
async def native(callback : CallbackQuery):
    await callback.answer('Вы выбрали Нативную разработку.')
    await callback.message.answer(inf_native)


@router.callback_query(F.data == 'Кроссплатформенная')
async def crossplatform(callback : CallbackQuery):
    await callback.answer('Вы выбрали Кроссплатформенную разработку.')
    await callback.message.answer(inf_crossplatfrom)

@router.callback_query(F.data == 'Игровая')
async def gaming(callback : CallbackQuery):
    await callback.answer('Вы выбрали Игровую разработку.')
    await callback.message.answer(inf_gaming)

@router.callback_query(F.data == 'Experience')
async def experience(callback : CallbackQuery):
    await callback.answer('Вы выбрали User Experience.')
    await callback.message.answer(inf_experiance)



@router.callback_query(F.data == 'Interface')
async def interface(callback : CallbackQuery):
    await callback.answer('Вы выбрали User Interface.')
    await callback.message.answer(inf_experiance)



