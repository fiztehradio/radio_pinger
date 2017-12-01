#!/usr/bin/python
# coding: utf8

from gopro.gopro import GoPro

class Gopro(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.camera = GoPro.GoPro()
        if not self.camera.status["ok"]:
            print("Connection Failed")
        self.ready = self.camera.status["ok"]

    def take_photo(self, path):
        self.camera.photo()
        self.camera.capture()
        self.save_photo(path)
        return True

    def save_photo(self, path):
        self.camera.media[-1].save(path)
