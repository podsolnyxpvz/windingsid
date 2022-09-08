import telebot 
import logging
import random
import sqlite3
import time
import datetime
import requests
import configparser
import random
import re
import sys
import telebot.apihelper
import telebot.util
import config
import datetime as DT
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(config.TOKEN)
connect = sqlite3.connect('db/bot.db')

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message, f'''👋Приветствую {message.from_user.first_name}👋!\n\nНазовите будущее название для лавки с *🌯ШАУРМОЙ🌯!*''', parse_mode="Markdown")

@bot.message_handler(content_types=["text"])
def tools(message):
	  connect = sqlite3.connect('db/bot.db')
	  cursor = connect.cursor()
	  cursor.execute("""CREATE TABLE IF NOT EXISTS shops(shop TEXT,owner TEXT)""")
	  connect.commit()
	  people_id = message.chat.id
	  cursor.execute(f"SELECT shop FROM shops WHERE shop = {people_id}")
	  shop = [message.text]
	  data = cursor.fetchone()
	  if data is None:
	   		cursor.execute("INSERT INTO shops VALUES(?, ?)", (shop))
	   		people_id = message.chat.id
	   		cursor.execute(f"SELECT owner FROM shops WHERE owner = {people_id}")
	   		username = [message.from_user.username]
	   		data = cursor.fetchone()
	   		if data is None:
	   			cursor.execute("INSERT INTO shops VALUES(?, ?)", (username))
	   			connect.commit()

bot.infinity_polling(none_stop=True)