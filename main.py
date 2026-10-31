import telebot, urllib.parse, os
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot Online 24/7! Eb3at ay wasf")

@bot.message_handler(func=lambda m: True)
def img(m):
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(m.text)}?width=1024&height=1024"
    bot.send_photo(m.chat.id, url)

bot.infinity_polling()
