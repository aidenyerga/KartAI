import Global as glv
import Player as player
import Timer as timer
import StateManager as sm
import Controls as controls
import Points as points

def init():
    global q
    global a
    global y

    q = [[0.0 for x in range(3)] for y in range(int(2**(len(sm.state))))]
  
    a = 0.1
    y = 0.9

#### Calcs state index ####
def calcstate():
    st = 0
    for n in range(0, len(sm.state)):
        st = st+(2**n)*int(sm.state[n])
    return st

#### Makes action selection based on q ####
def select_action(state, rand):
    global q
    
    selected_action = 0
    val = -float("inf")
    for n in range(0, 3):
        if (q[state][n] > val):
            val = q[state][n]
            selected_action = n
    
    if (rand and random(0, 100) >= 99):
        selected_action = floor(random(0, 3))
    
    return selected_action

def perform_action(action):
    if (action == 1):
        controls.turnLeft()
    if (action == 2):
        controls.turnRight()
        
    timer.run()
    player.updatePos()
    player.checkBounds()
    sm.calcTestpoints()
    sm.updateState()

def qlearn():
    global q
    global a
    global y
    
    current_state = calcstate()
    action = select_action(current_state, True)
    
    perform_action(action)
    
    #### Update q ####
    if (not glv.BlockLearning):
        reward = points.getReward(action)
        
        fstate = calcstate()
        faction = select_action(fstate, False)
        current_state_value = q[current_state][action]
        q[current_state][action] = (1.0-a)*q[current_state][action] + a*(reward+y*q[fstate][faction])
        #print("ESTADO :" + str(current_state) + " Q= " + str(current_state_value) + " ACTUALIZADO CON " + str(q[current_state][action]))
        #print("--------------------")
    
    