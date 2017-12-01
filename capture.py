#!/usr/bin/python
# coding: utf8

from gopro.gopro import GoPro
from time import sleep

class Gopro(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.camera = GoPro.GoPro()
        if not self.camera.status["ok"]:
            print("Connection Failed")
        self.ready = self.camera.status["ok"]
        self.state = set([m.basename for m in self.camera.media])


    def take_photo(self, path):
        self.camera.photo()
        self.camera.capture()
        print("path", path)
        return self.save_photo(path)

    def save_photo(self, path):

        current_state = set([m for m in self.camera.media])
        new_imgs = [x for x in self.camera.media if x.basename not in self.state]

        # for image in self.camera.media:
        #     image.save(path + "backup/" + image.basename);

        print("new images",[img.basename for img in new_imgs])
        if len(new_imgs) == 0:
            print("SOOOOQA")
            return
        for m in new_imgs:
            m.save(path + "capture.jpg")
            m.save(path + m.basename)
            print("path", path)

        self.state = set([m.basename for m in self.camera.media])

        return path + "capture.jpg"
