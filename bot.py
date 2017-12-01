#!/usr/bin/python
# coding: utf8

import telebot
import subprocess

fradio_chat_id = 0
with open("data/fiztehradio.chatid", "r") as file:
	fradio_chat_id = file.read().strip()

with open("data/phystechbot.token", "r") as file:
	token = file.read().strip()
	bot = telebot.TeleBot(token)

print("Started bot with token /"+token+"/")

path_to_photo = "/Users/fiztehradio/Camera/rubka.png"
sooq_sticker1 = "CAADAgADIgAD1vl9CIhY2t5j3nJoAg"
sooq_sticker2 = "CAADAgADIwAD1vl9CF9PaiN4TXvCAg"
delay = 0

def take_photo(wait=0):
	command = "imagesnap %s" % path_to_photo
	if wait:
		command += " -w %f" % wait
	proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = proc.communicate()
	if error is not None:
		print (error)
		return False
	return True


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['photo']) # func=lambda m: m == "photo")
def send_photo(message):
	if fradio_chat_id != message.chat.id:
		bot.send_message(message.chat.id, u"Вы не в чате команды Физтех.Радио. Сори :(")
		return
	if take_photo(wait=delay):
		with open(path_to_photo, 'rb') as photo:
			bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['sooq']) # func=lambda m: m == "photo")
def send_sooqa(message):
	bot.send_sticker(message.chat.id, sooq_sticker1)

@bot.message_handler(commands=['sooqa']) # func=lambda m: m == "photo")
def send_sooqa(message):
	bot.send_sticker(message.chat.id, sooq_sticker2)

bot.polling()
