#!/usr/bin/env python2.7
# coding: utf8

import telebot
import subprocess

from consts import *
from capture import Gopro


bot = None
fradio_chat_id = None
token = None
capture = None


with open(fizteh_chat_id_path, "r") as file:
    fradio_chat_id = file.read().strip()

print("FIZTEH RADIO token is /"+fradio_chat_id+"/")

with open(bot_token, "r") as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)
print("Started bot with token /" + token + "/")

capture = Gopro()
if not capture.ready:
    print("Can't init Gopro")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['photo'])
def send_photo(message):
    if fizteh_chat_only and fradio_chat_id != message.chat.id:
        bot.send_message(
            message.chat.id, u"Вы не в чате команды Физтех.Радио. Сори :(")
        return
    path = capture.take_photo(path_to_photo)
    if path:
        print("path_to_photo", path)
        with open(path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['sooq', 'sooqa', 'soooq'])
def send_sooqa(message):
    bot.send_sticker(message.chat.id, sooq_sticker1)


bot.polling()
