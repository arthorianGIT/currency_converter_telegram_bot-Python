import telebot
from currency_converter import CurrencyConverter
from dotenv import load_dotenv
import os

load_dotenv('.env')
bot_key = os.getenv('bot_key')

converter = CurrencyConverter()
bot = telebot.TeleBot(bot_key)

