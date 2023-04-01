import telebot
from .openai import send_request
from decouple import config

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
SAMUEL_ID = int(config('SAMUEL_ID'))
DAIANA_ID = int(config('DAIANA_ID'))

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "How are you doing?")

# Handle all other messages with content_type 'text'
@bot.message_handler(func=lambda m: True)
def handle_messsage(message):
    if message.from_user.id not in [SAMUEL_ID, DAIANA_ID]:
        bot.reply_to(message, "I'm sorry, I can't talk to you.")
        return
    prompt = message.text
    response = send_request(prompt)
    bot.reply_to(message, response)

def start_bot():
    bot.infinity_polling()