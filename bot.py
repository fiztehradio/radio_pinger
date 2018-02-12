#!/usr/bin/env python2.7
# coding: utf8

import telegram

from consts import *
from stream_status import check_stream

with open(fizteh_chat_id_path, "r") as file:
    fradio_chat_id = file.read().strip()

print("FIZTEH RADIO token is /"+fradio_chat_id+"/")

with open(bot_token, "r") as f:
    token = f.read().strip()

bot = telegram.Bot(token)
print("Started bot with token /" + token + "/")

is_alive = check_stream()
if not is_alive:
    bot.send_message(
        chat_id=fradio_chat_id,
        text="Походу, радио сдохло! Проверьте: http://radio.mipt.ru"
    )
