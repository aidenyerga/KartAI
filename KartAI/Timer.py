# KartAI https://github.com/eritzyg/KartAI/
# Copyright (c) 2017 Eritz Yerga Gutierrez and Iker García Ferrero
# MIT License https://github.com/eritzyg/KartAI/blob/master/LICENSE

import Global as glv

def init():
    
    global frames
    global best
    global started
    
    frames = 0.0
    best = 0.0
    started = True
    
def startt():
    global started
    started = True
    
def pauset():
    global started
    started = False
    
def reset():
    global frames
    global best
    if (frames > best):
        best = frames
    frames = 0.0
    
def run():
    global frames
    global started
    if (started):
        frames = frames+1
    