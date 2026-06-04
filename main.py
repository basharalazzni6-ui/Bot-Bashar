import telebot

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 البوت شغال!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
