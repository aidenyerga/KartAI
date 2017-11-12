# KartAI https://github.com/eritzyg/KartAI/
# Copyright (c) 2017 Eritz Yerga Gutierrez and Iker García Ferrero
# MIT License https://github.com/eritzyg/KartAI/blob/master/LICENSE

import Global as glv
import Render as render
import TrackManager as tm
import Timer as timer

def init():
    #Player data
    global posx
    global posy
    global current_sector
    global last_sector
    global dir
    global velocity
    global rotation
    global innerce
    global isAlive
    global isAI
    
    #### Init player data ####
    tm.initplayer()
    innerce = 0.0
    isAlive = True
    isAI = True
    
def updatePos():
    #Player data
    global posx
    global posy
    global dir
    global velocity
    global rotation
    global innerce
    
    #### Direction calc ####
    rotation_to_radians = radians(rotation)
    dir[0] = cos(rotation_to_radians)
    dir[1] = -sin(rotation_to_radians)
    
    if (dir[0] < 0.0001 and dir[0] > -0.0001):
        dir[0] = 0.0
    if (dir[1] < 0.0001 and dir[1] > -0.0001):
        dir[1] = 0.0
    
    #### Rotation update calc ####
    if (rotation > 360.0):
        rotation = rotation-360.0
    if (rotation < 0.0):
        rotation = 360.0+rotation
    rotation = rotation+1.0*(innerce/30.0)
    
    if (velocity > 2.0):
        velocity = 2.0
    if (velocity < 0.2):
        velocity = 0.2
    
    #### Position update calc ####
    posx = posx+dir[0]*velocity
    posy = posy+dir[1]*velocity
    
    #### Innerce reset calc ####
    if (glv.press == 0):
        innerce = innerce-(innerce/10.0)
        if (innerce < 0.0001 and innerce > -0.0001):
            innerce = 0.0
    if (glv.press > 0):
        glv.press = glv.press-1
        
def checkBounds():
    global posx
    global posy
    global isAlive
    if (glv.EnableTrackmap and not getTrackmap()):
        isAlive = False

def getTrackmap():
    global posx
    global posy
    global current_sector
    
    # /!\ If trackmap disabled it will always return true /!\ #
    if (not glv.EnableTrackmap):
        return True
    
    c = render.trackmap.pixels[int(posx)+int(posy)*1024]
    
    if (floor(red(c)) == 0 and floor(green(c)) == 255):
        if (floor(blue(c)) == 255):
            glv.FLC = True
        else:
            if (glv.FLC):
                print(" # Finish line crossed at try "+str(glv.Try)+". Timestamp: "+str(timer.frames)+" frames.")
                glv.FLC = False
        return True
    else:
        return False