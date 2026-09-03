import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Добро пожаловать в IshBorBot!\n\n"
        "Здесь будут задания и возможности заработать."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Скоро здесь появятся задания. 🔥")

bot.infinity_polling()
