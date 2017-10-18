import Global as glv
import Player as player
import TrackManager as tm
import Timer as timer
import Points as points

def turnLeft():
    if (not player.isAlive): return
    glv.press = 2
    if (player.innerce < 30.0):
        if (player.innerce < 0.0):
            player.innerce = player.innerce+25.0
        player.innerce = player.innerce+25.0
        
def turnRight():
    if (not player.isAlive): return
    glv.press = 2
    if (player.innerce > -30.0):
        if (player.innerce > 0.0):
            player.innerce = player.innerce-25.0
        player.innerce = player.innerce-25.0

def accel():
    if (not player.isAlive): return
    player.velocity = player.velocity+0.1

def deccel():
    if (not player.isAlive): return
    player.velocity = player.velocity-0.1
    
def reset():
    tm.ldTrack()
    timer.reset()
    points.points = 0.0
    player.innerce = 0.0
    player.isAlive = True
    glv.press = 0
    glv.ForceReset = False