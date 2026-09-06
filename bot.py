import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Балансы пользователей
balances = {}


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id

    if user_id not in balances:
        balances[user_id] = 0

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton("🎥 Смотреть видео"),
        types.KeyboardButton("💰 Баланс")
    )
    keyboard.add(
        types.KeyboardButton("📋 Задания")
    )

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в IshBorBot!\n\n"
        "Здесь ты сможешь выполнять задания и получать вознаграждения.",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda message: message.text == "💰 Баланс")
def balance(message):
    user_id = message.from_user.id
    amount = balances.get(user_id, 0)

    bot.send_message(
        message.chat.id,
        f"💰 Твой баланс: {amount} сум"
    )


@bot.message_handler(func=lambda message: message.text == "📋 Задания")
def tasks(message):
    bot.send_message(
        message.chat.id,
        "📋 Доступные задания:\n\n"
        "Пока заданий нет.\n"
        "🔥 Скоро здесь появятся новые задания!"
    )


@bot.message_handler(func=lambda message: message.text == "🎥 Смотреть видео")
def videos(message):
    bot.send_message(
        message.chat.id,
        "🎥 Видео пока нет.\n\n"
        "Скоро здесь появятся видео с вознаграждением."
    )


@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.send_message(
        message.chat.id,
        "Используй кнопки меню 👇"
    )


bot.infinity_polling()