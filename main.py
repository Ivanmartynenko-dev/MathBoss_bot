
import os  # Модуль для работы с операционной системой, в частности, для получения переменных окружения
import asyncio  # Модуль для работы с асинхронными операциями
import logging  # Модуль для ведения логов (отслеживание и запись работы программы)
from aiogram import Bot, Dispatcher  # Импорт классов для создания бота и диспетчера сообщений
from dotenv import load_dotenv  # Импорт функции для загрузки переменных окружения из файла .env
from aiogram import types  # Импортирует типы данных из библиотеки aiogram (например, для сообщений)
from aiogram.filters import CommandStart  # Импорт фильтра для команды "/start"
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import game
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
# Загрузка переменных окружения из файла .env
load_dotenv()

class GameStates(StatesGroup):
    waiting_for_answer = State()

# Инициализация объекта бота, токен берется из переменной окружения BOT_TOKEN
bot = Bot(os.getenv('API_KEY'))

# Инициализация диспетчера для управления событиями и сообщениями
dp = Dispatcher()

# Обработчик команды "/start"
@dp.message(CommandStart())
async def handle_start(mess: types.Message):
    # Отправка приветственного сообщения с именем пользователя, который вызвал команду
    await mess.answer(text=f"Привет, {mess.from_user.full_name}! Готов решать примеры?")


@dp.message()
async def send_primer(mess:types.Message, state: FSMContext):
    if 'да' in mess.text.lower():
        a = game.level_1()
        primer = a[0]+a[1]+a[2]
        otvet = a[3]
        await mess.answer(primer)
        await state.update_data(correct = otvet)
        await state.set_state(GameStates.waiting_for_answer)
@dp.message(GameStates.waiting_for_answer, )
async def send_otvet(mess:types.Message, state: FSMContext):
    print('GJHFJHGJFHKJGHF')
    user_data = await state.get_data()
    correct_answer = user_data['correct']
    print(correct_answer)
    print(mess.text)
    try:
        if int(mess.text) == int(correct_answer):
            await mess.answer("Правильно!")
        else:
            await mess.answer(f'Неправильно( Правильный ответ был {correct_answer}. Попробуй другой пример')
    except ValueError:
        await mess.answer("Необходим числовой ответ")
    await state.finish()
# Основная асинхронная функция программы
async def main():
    # Настройка логирования, чтобы выводить сообщения с уровнем INFO и выше
    logging.basicConfig(level=logging.INFO)
    
    # Запуск процесса опроса сообщений от пользователей
    await dp.start_polling(bot)

# Проверка, что скрипт запущен напрямую
if __name__ == '__main__':
    # Запуск основного асинхронного процесса
    asyncio.run(main())