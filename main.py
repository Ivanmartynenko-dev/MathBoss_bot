
import os  # Модуль для работы с операционной системой, в частности, для получения переменных окружения
import asyncio  # Модуль для работы с асинхронными операциями
import logging  # Модуль для ведения логов (отслеживание и запись работы программы)
from aiogram import Bot, Dispatcher  # Импорт классов для создания бота и диспетчера сообщений
from dotenv import load_dotenv  # Импорт функции для загрузки переменных окружения из файла .env
from aiogram import types  # Импортирует типы данных из библиотеки aiogram (например, для сообщений)
from aiogram.filters import CommandStart  # Импорт фильтра для команды "/start"
from aiogram.utils.keyboard import InlineKeyboardBuilder

import game
# Загрузка переменных окружения из файла .env
load_dotenv()

# Инициализация объекта бота, токен берется из переменной окружения BOT_TOKEN
bot = Bot(os.getenv('API_KEY'))

# Инициализация диспетчера для управления событиями и сообщениями
dp = Dispatcher()

# Обработчик команды "/start"
@dp.message(CommandStart())
async def handle_start(mess: types.Message):
    # Отправка приветственного сообщения с именем пользователя, который вызвал команду
    await mess.answer(text=f"Привет, {mess.from_user.full_name}!")
# Основная асинхронная функция программы
@dp.callback_query(lambda call: True)
async def  callback(call:types.CallbackQuery):
    if call.data == 'bytton1':
        await call.message.answer(
            'Вы нажали кнопку 1'
        )
    else:
        await call.message.answer(
            'Вы нажали кнопку 2'
        )
async def main():
    # Настройка логирования, чтобы выводить сообщения с уровнем INFO и выше
    logging.basicConfig(level=logging.INFO)
    
    # Запуск процесса опроса сообщений от пользователей
    await dp.start_polling(bot)

# Проверка, что скрипт запущен напрямую
if __name__ == '__main__':
    # Запуск основного асинхронного процесса
    asyncio.run(main())