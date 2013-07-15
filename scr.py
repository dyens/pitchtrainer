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
    table_notes = [
            u'До',  #0 
            u'#'    #1
            u'Ре',  #2
            u'#'    #3
            u'Ми',  #4
            u'Фа',  #5
            u'#',   #6
            u'Соль',#7
            u'#',   #8
            u'Ля',  #9
            u'#',   #10 
            u'Си'   #11 
            ]

    table_files = {
            'A3-220.0.mp3': [9, 3, 220.0],
            'Asharp3-233.08.mp3': [10, 3, 233.08],
            'B3-246.94.mp3': [11, 3, 246.94],
            'C4-261.63.mp3': [0, 4, 261.63],
            'Csharp4-277.18.mp3': [1, 4, 277.18],
            'D4-293.66.mp3': [2, 4, 293.66],
            'Dsharp4-311.13.mp3': [3, 4, 311,13],
            'E4-329.63.mp3': [4, 4, 329.63],
            'F4-349.23.mp3': [5, 4, 349.23],
            'G4-392.0.mp3': [7, 4, 392.0],
            'A4-440.0.mp3': [9, 4, 440.0],
            'Asharp4-466.16.mp3': [10, 4, 466.16],
            'B4-493.88.mp3': [11, 4, 493.88],
            'C5-523.25.mp3': [0, 5, 523.25],
            'Csharp5-554.37.mp3': [1, 5, 554.37],
            'D5-587.33.mp3': [2, 5, 587.33],
            'Dsharp5-622.25.mp3': [3, 5, 622],
            'E5-659.26.mp3': [4, 5, 659],
            'Fsharp4-369.99.mp3': [6, 4, 369.99],
            'Gsharp4-415.3.mp3': [8, 4, 415.4]
            }

    path = os.path.abspath(os.path.dirname(__file__))
    music_path = os.path.join(path, 'music')

    def filefinder(self):
        #TODO:scan only mp3 files. 
        #TODO:Add another parameters(guitar sound, piano, duration..)
        for f in listdir(self.music_path):
            yield f

    def play_random_notes(self):
        self.music = [f for f in self.filefinder()]
        i = 50
        while True:
            i+=1
            filenote = random.choice(self.music[0:i/50+1])
            print i
            print self.music[0:i/50+1]
            note = filenote.split('.')[0]
            path = os.path.join(self.music_path, filenote)
            Popen('mpg123 %s' %path, shell=True)
            Popen("notify-send %s" %note, shell=True)
            time.sleep(10)


    def test1(self):
        '''
        Only CDEFGAB in one octave
        '''

        self.table_music = {}
        for i in self.table_files:
            if self.table_files[i][0] not in [1,3,6,8,10] and self.table_files[i][1] == 4 :
                self.table_music[i] = self.table_files[i]

    def test2(self):
        '''
        Only CDEFGAB
        '''

        self.table_music = {}
        for i in self.table_files:
            if self.table_files[i][0] not in [1,3,6,8,10]:
                self.table_music[i] = self.table_files[i]

    def play(self):
        self.music = [f for f in self.table_music]
        print self.music
        while True:
            filenote = random.choice(self.music)
            note = filenote.split('.')[0]
            path = os.path.join(self.music_path, filenote)
            Popen('mpg123 %s' %path, shell=True)
            Popen("notify-send %s" %note, shell=True)
            time.sleep(10)

if __name__ == "__main__":
    p = Player()
    p.test1()
    p.play()
