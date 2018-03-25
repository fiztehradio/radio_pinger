#!/usr/bin/env python2.7
# coding: utf8

import random
import telegram

from consts import *
from stream_status import check_stream

def reply_sticker(sticker_id):
    bot.send_sticker(chat_id=fradio_chat_id, sticker=sticker_id)

def reply_text(text):
    bot.send_message(chat_id=fradio_chat_id, text=text)

def reply_broken_radio():
    actions = [
        lambda: reply_text("Походу, радио сдохло! Проверьте: http://radio.mipt.ru"),
        lambda: reply_text("@mierokhin, радио кажись сделало сибастиена из эфира! Разберись с этим: http://radio.mipt.ru"),
        lambda: reply_text("@Exferro, радио из дэд. Разберись с этим: http://radio.mipt.ru"),
        lambda: reply_text("@ivanpotylitcyn, радио из дэад. Разберись с этим: http://radio.mipt.ru"),
        lambda: reply_sticker(broken_radio_sticker1),
        lambda: (reply_text("не работает http://radio.mipt.ru"), reply_sticker(broken_radio_sticker2)),
        lambda: (reply_text("радио не работает"), reply_sticker(broken_radio_sticker3)),
        lambda: (reply_text("радио не работает :С :С :С"), reply_sticker(broken_radio_sticker2))
    ]
    random.choice(actions)()

with open(fizteh_chat_id_path, "r") as file:
    fradio_chat_id = file.read().strip()

print("FIZTEH RADIO token is /"+fradio_chat_id+"/")

with open(bot_token, "r") as f:
    token = f.read().strip()

bot = telegram.Bot(token)
print("Started bot with token /" + token + "/")

is_alive = check_stream()
if not is_alive:
    reply_broken_radio()
