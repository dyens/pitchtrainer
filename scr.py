#!/usr/bin/env python
# coding: utf-8
'''
File    : scr.py
Author  : Kapustin A. S.
Contact : a.kapustin@spbu.ru
Date    : 2013 Июл 12

Description : Program for training musical pitch.
'''
from subprocess import Popen, PIPE
import os.path
from os import listdir
import time
import random

#Popen("mpg123 test.mp3", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
class Player(object):
    '''
    Main class for initialization and start porgram

    '''
    path = os.path.abspath(os.path.dirname(__file__))
    music_path = os.path.join(path, 'music')

    def filefinder(self):
        #TODO:scan only mp3 files. 
        #TODO:Add another parameters(guitar sound, piano, duration..)
        for f in listdir(self.music_path):
            yield f

    def play(self):
        self.music = [f for f in self.filefinder()]
        while True:
            filenote = random.choice(self.music)
            note = filenote.split('.')[0]
            path = os.path.join(self.music_path, filenote)
            Popen('mpg123 %s' %path, shell=True)
            Popen("notify-send %s" %note, shell=True)
            time.sleep(10)

if __name__ == "__main__":
    p = Player()
    p.play()
