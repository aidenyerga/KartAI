# KartAI https://github.com/eritzyg/KartAI/
# Copyright (c) 2017 Eritz Yerga Gutierrez and Iker García Ferrero
# MIT License https://github.com/eritzyg/KartAI/blob/master/LICENSE

import Global as glv
import Player as player
import StateManager as sm
import TrackManager as tm
import Timer as timer
import Points as points

def init():
    #Fonts
    global font
    font = createFont("Hooge0553", 18)
    
    #Sprites
    global car
    global track
    
    #Track zone map
    global trackmap
    
    #Sprite display scaling
    global displayscale
    
    #### Load sprites ####
    car = loadImage("car.png")
    tm.initrender()
    
    #### Set sprite display scaling (ONLY INTEGER SCALING) ####
    displayscale = 5

#### Render mode 0 with zoom ####
def drawSprites():
    #Sprites
    global car
    global track
    
    #Sprite display scaling
    global displaycale
    
    #### Display track ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(player.rotation-90.0))
    translate(-width/2, -height/2)
    image(track, -(player.posx*displayscale)+(width/2), -(player.posy*displayscale)+(height/2), 1024*displayscale, 1024*displayscale)
    if (glv.renderTrackmap):
        image(trackmap, -(player.posx*displayscale)+(width/2), -(player.posy*displayscale)+(height/2), 1024*displayscale, 1024*displayscale)
    popMatrix()
    #### Display player car ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(-player.innerce))
    translate(-width/2, -height/2)
    image(car, (width/2)-10*displayscale, (height/2)-22*displayscale, 21*displayscale, 45*displayscale)
    popMatrix()
    #### Render collision lines if enabled ####
    if (glv.renderCollisionLines):
        pushMatrix()
        translate(width/2, height/2)
        rotate(radians(player.rotation-90.0))
        translate(-width/2, -height/2)
        sm.renderTestlines()
        popMatrix()

#### Render mode 0 without zoom ####
def drawSpritesNoScale():
    #Sprites
    global car
    global track
    
    #### Display track ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(player.rotation-90.0))
    translate(-width/2, -height/2)
    image(track, -player.posx+(width/2), -player.posy+(height/2))
    if (glv.renderTrackmap):
        image(trackmap, -player.posx+(width/2), -player.posy+(height/2))
    popMatrix()
    #### Display player car ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(-player.innerce))
    translate(-width/2, -height/2)
    image(car, (width/2)-10, (height/2)-22)
    popMatrix()
    #### Render collision lines if enabled ####
    if (glv.renderCollisionLines):
        pushMatrix()
        translate(width/2, height/2)
        rotate(radians(player.rotation-90.0))
        translate(-width/2, -height/2)
        sm.renderTestlinesNoScale()
        popMatrix()

#### Render mode 1 with zoom ####
def drawSpritesAltRenderer():
    #Sprites
    global car
    global track
    
    #Sprite display scaling
    global displaycale
    
    #### Display track ####
    image(track, -(player.posx*displayscale)+(width/2), -(player.posy*displayscale)+(height/2), 1024*displayscale, 1024*displayscale)
    if (glv.renderTrackmap):
        image(trackmap, -(player.posx*displayscale)+(width/2), -(player.posy*displayscale)+(height/2), 1024*displayscale, 1024*displayscale)
    #### Display player car ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(90.0-player.rotation))
    rotate(radians(-player.innerce))
    translate(-width/2, -height/2)
    image(car, (width/2)-10*displayscale, (height/2)-22*displayscale, 21*displayscale, 45*displayscale)
    popMatrix()
    #### Render collision lines if enabled ####
    if (glv.renderCollisionLines):
        sm.renderTestlines()

#### Render mode 1 without zoom ####
def drawSpritesNoScaleAltRenderer():
    #Sprites
    global car
    global track
    
    #### Display track ####
    image(track, -player.posx+(width/2), -player.posy+(height/2))
    if (glv.renderTrackmap):
        image(trackmap, -player.posx+(width/2), -player.posy+(height/2))
    #### Display player car ####
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(90.0-player.rotation))
    rotate(radians(-player.innerce))
    translate(-width/2, -height/2)
    image(car, (width/2)-10, (height/2)-22)
    popMatrix()
    #### Render collision lines if enabled ####
    if (glv.renderCollisionLines):
        sm.renderTestlinesNoScale()

#### HUD Renderer ####
def drawHUD():
    #Font
    global font
    
    #### HUD Draw ####
    textFont(font, 18)
    textAlign(LEFT)
    textWithBorders("Position: ("+str(player.posx)+", "+str(player.posy)+")", 30, 30)
    textWithBorders("Velocity: "+str(player.velocity)+" Innerce: "+str(player.innerce)+" Rotation: "+str(player.rotation), 30, 50)
    textWithBorders("Direction: "+str(player.dir[0])+", "+str(player.dir[1])+" isAlive: "+str(player.isAlive), 30, 70)
    textWithBorders("State: "+str(sm.state)+" Distfront: "+str(sm.distfront), 30, 90)
    textWithBorders("FPS: "+str(frameRate)+" EventDelta: "+str(glv.eventDelta), 30, 110)
    if (glv.press > 0):
        textWithBorders("Press considered", 30, 140)

#### Timer renderer ####   
def drawTimer():
    #Font
    global font
    
    #### Draw Timer ####
    textFont(font, 18)
    textAlign(RIGHT)
    textWithBorders(tm.tracknames[tm.selectedTrack], width-23, 23)
    textWithBorders("TIME "+str(int(timer.frames)), width-23, 42)
    textWithBorders("BEST TIME "+str(int(timer.best)), width-23, 60)
    textWithBorders("REWARD "+str(int(points.points)), width-23, 80)
    
    
def textWithBorders(txt, x, y):
    fill(0)
    text(txt, x-1, y)
    text(txt, x-1, y-1)
    text(txt, x, y-1)
    text(txt, x+1, y)
    text(txt, x+1, y+1)
    text(txt, x, y+1)
    fill(255)
    text(txt, x, y)
    
def getTrackmap(x, y):
    # /!\ If trackmap disabled it will always return true /!\ #
    if (not glv.EnableTrackmap):
        return True
    
    global trackmap
    
    c = trackmap.pixels[int(x)+int(y)*1024]
    
    if (floor(red(c)) == 0 and floor(green(c)) == 255):
        return True
    else:
        return False