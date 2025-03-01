import telebot
from currency_converter import CurrencyConverter
from dotenv import load_dotenv
import os

load_dotenv('.env')
bot_key = os.getenv('bot_key')

converter = CurrencyConverter()
bot = telebot.TeleBot(bot_key)

@bot.message_handler(commands=['start'])
def start(message):
    reply = telebot.types.ReplyKeyboardMarkup()
    reply.add(telebot.types.KeyboardButton('Convert Currencies'))
    reply.add(telebot.types.KeyboardButton('Watch Currencies'))
    bot.send_message(message.chat.id, "Hello! I'm bot that can convert currencies!")
    bot.send_message(message.chat.id, 'You can convert currencies by clicking button in the menu', reply_markup=reply)

@bot.message_handler(func=lambda message: message.text in ('Convert Currencies', 'Watch Currencies'))
def menu_functions(message):
    if message.text.lower().strip() == 'convert currencies':
        bot.send_message(message.chat.id, '''Okay! So type your currency!\n<b>In that format ('amount' 'base_currency' to 'target_currency')</b>''', parse_mode='html')
        bot.register_next_step_handler(message, convert_value)
    elif message.text.lower().strip() == 'watch currencies':
        bot.send_message(message.chat.id, ''''DKK', 'HUF', 'ROL', 'RON', 'SEK', 'EUR', 'RUB', 'JPY', 'PHP', 'MTL', 'TRY', 'BRL', 'ILS', 'SKK', 'SIT', 'HKD', 'LVL', 'PLN', 'INR', 'NOK', 'CYP', 'CHF', 'NZD', 'TRL', 'KRW', 'CNY', 'USD', 'MYR', 'SGD', 'THB', 'GBP', 'AUD', 'BGN', 'MXN', 'ISK', 'CZK', 'EEK', 'IDR', 'ZAR', 'LTL', 'CAD', 'HRK''''')

def convert_value(message):
    split_message = message.text.split()
    amount = split_message[0]
    base_currency = split_message[1].upper()
    target_currency = split_message[3].upper()
    converted = converter.convert(amount, base_currency, target_currency)
    bot.reply_to(message, f'Here is your complete convert: {converted:.2f} {target_currency}')

bot.infinity_polling()
