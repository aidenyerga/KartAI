# KartAI https://github.com/eritzyg/KartAI/
# Copyright (c) 2017 Eritz Yerga Gutierrez and Iker García Ferrero
# MIT License https://github.com/eritzyg/KartAI/blob/master/LICENSE

import Global as glv
import TrackManager as tm
import Render as render
import Player as player
import Controls as controls
import StateManager as sm
import Timer as timer
import Points as points
import QLearning as qlearn

def setup():
    #### Init ####
    size(1280, 720)
    
    glv.init()
    tm.init()
    render.init()
    player.init()
    sm.init()
    timer.init()
    points.init()
    qlearn.init()

    #### End init ####
    frameRate(999)
    noSmooth()
    if (glv.EnableTrackmap):
        loadPixels()
        render.trackmap.loadPixels()
    
def draw():
    glv.eventDelta = 1.0/frameRate

    #### Render sprites ####
    background(0)
    if (glv.renderer == 1):
        if (not glv.disableScaling):
            render.drawSprites()
        else:
            render.drawSpritesNoScale()
    if (glv.renderer == 2):
        if (not glv.disableScaling):
            render.drawSpritesAltRenderer()
        else:
            render.drawSpritesNoScaleAltRenderer()
    
    #### AI actions and physics ####
    if (player.isAlive):
        if (player.isAI):
            qlearn.qlearn()
            if (glv.ForceReset):
                controls.reset()
            if (not player.isAlive):
                print("-AI died in try "+str(glv.Try)+". Timestamp: "+str(timer.frames)+" frames.")
                glv.Try = glv.Try+1
                controls.reset()
        else:
            timer.run()
            player.updatePos()
            player.checkBounds()
            sm.calcTestpoints()
            sm.updateState()
            if (not player.isAlive or glv.ForceReset):
                controls.reset()
    
    #### Render HUD ####
    if (glv.HUDEnabled):
        render.drawHUD()
        render.drawTimer()

#### Controls handler ####
def keyPressed():
    if (not player.isAI):
        if (key == 'a' or key == 'A'):
            controls.turnLeft()
        if (key == 'd' or key == 'D'):
            controls.turnRight()
        if (key == 'w' or key == 'W'):
            controls.accel()
        if (key == 's' or key == 'S'):
            controls.deccel()
        if (key == ' '):
            controls.reset()
    if (key == 'z' or key == 'Z'):
        glv.disableScaling = not glv.disableScaling
    if (key == 'h' or key == 'H'):
        glv.HUDEnabled = not glv.HUDEnabled
    if (key == 'm' or key == 'M'):
        glv.renderTrackmap = not glv.renderTrackmap
    if (key == 'l' or key == 'L'):
        glv.renderCollisionLines = not glv.renderCollisionLines
    if (key == 'r' or key == 'R'):
        if (glv.renderer == 0):
            glv.renderer = 1
        else:
            if (glv.renderer == 1):
                glv.renderer = 2
            else:
                if (glv.renderer == 2):
                    glv.renderer = 0
    if (key == 'n' or key == 'N'):
        glv.BlockLearning = not glv.BlockLearning
        print("*BlockLearning set to: "+str(glv.BlockLearning))
    if (key == '0'):
        tm.setTrack(0)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '1'):
        tm.setTrack(1)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '2'):
        tm.setTrack(2)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '3'):
        tm.setTrack(3)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '4'):
        tm.setTrack(4)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '5'):
        tm.setTrack(5)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '6'):
        tm.setTrack(6)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '7'):
        tm.setTrack(7)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '8'):
        tm.setTrack(8)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])
    if (key == '9'):
        tm.setTrack(9)
        glv.ForceReset = True
        print("Loaded track: "+tm.tracknames[tm.selectedTrack])