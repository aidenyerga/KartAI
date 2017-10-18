import Player as player
import StateManager as sm
import Timer as timer
    
def init():
    global points
    
    points = 0.0

#### Reward function for Q-Learning ####
def getReward(action):
    global points
    
    points = 10.0
    if (player.isAlive):
        if (sm.state[0] or sm.state[1] or sm.state[2] or sm.state[3] or sm.state[4] or sm.state[5] or sm.state[6]):
            points = points-5.0-(1.0-sm.distfront)*60.0
        else:
            if (action == 0):
                points = 20.0 
    else:
        points = -3000.0
    
    return points
    
    