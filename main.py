import telebot
from telebot import types
bot=telebot.TeleBot("7498922816:AAEVfH3FqfFvdw86CXw_QoqCj5qtAq09nOc")
@bot.message_handler(commands=["start"])
def Hello(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton(text="Базовая алгебра", url = 'https://en.wikipedia.org/wiki/Arithmetical_operation')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Приветствую! Я MathBoss. Попробуй пройти все мои уровни. Вся инфорция для их прохождения лежит тут", reply_markup = markup)



bot.polling(none_stop=True, interval=0)