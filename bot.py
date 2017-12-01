#!/usr/bin/python
# coding: utf8

import telebot
import subprocess

from consts import *
from capture import Gopro

with open(fizteh_chat_id_path, "r") as file:
	fradio_chat_id = file.read().strip()

with open(bot_token, "r") as file:
	token = file.read().strip()
	bot = telebot.TeleBot(token)

print("Started bot with token /"+token+"/")
capture = Gopro()
if not capture.ready:
	print("Can't init Gopro")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['photo']) # func=lambda m: m == "photo")
def send_photo(message):
	if fizteh_chat_only and fradio_chat_id != message.chat.id:
		bot.send_message(message.chat.id, u"Вы не в чате команды Физтех.Радио. Сори :(")
		return
	if capture.take_photo(path_to_photo):
		with open(path_to_photo, 'rb') as photo:
			bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['sooq']) # func=lambda m: m == "photo")
def send_sooqa(message):
	bot.send_sticker(message.chat.id, sooq_sticker1)

@bot.message_handler(commands=['sooqa']) # func=lambda m: m == "photo")
def send_sooqa(message):
	bot.send_sticker(message.chat.id, sooq_sticker2)

bot.polling()
