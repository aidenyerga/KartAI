import StateManager as sm
    
def init():
    global points
    points = 0.0

	
#### Reward function for Q-Learning ####
def getReward(action):
    global points
    
	 #Default 10 points
    points = 10.0
    if (player.isAlive):
        if (sm.state[0] or sm.state[1] or sm.state[2] or sm.state[3] or sm.state[4] or sm.state[5] or sm.state[6]):
		#If any sensor is active: points = 5 - (1.0 - distance to the wall [from 0.0 to 1.0] * 60.0)
            points = 5.0-(1.0-sm.distfront)*60.0
        else:
		#If action = Do nothing. Points = 20, this prevents the car the car from spining all the time and also accelerates the learning. 
            if (action == 0):
                points = 20.0 
    else:
		#If the car crash, huge penalty. 
        points = -3000.0
    
    return points
