import numpy as np
def dice_roll_markov_chain(startnumber):

    result=0

    State=[1,2,3,4,5,6]
    Outcome=[["11","12","13","14","15","16"],["21","22","23","24","25","26"],["31","32","33","34","35","36"],["41","42","43","44","45","46"],["51","52","53","54","55","56"],["61","62","63","64","65","66"]]
    probabilities=[[0.1,0.2,0.3,0.1,0.1,0.2],[0.1,0.2,0.3,0.1,0.1,0.2],[0,0.5,0.5,0,0,0],[0.1,0.2,0.3,0.1,0.1,0.2],[0.1,0.2,0.3,0.1,0.1,0.2],[0.1,0.2,0.3,0.1,0.1,0.2]]

    if startnumber==1:
        result = np.random.choice(State,p=probabilities[0])
    elif startnumber==2:
        result = np.random.choice(State, p=probabilities[1])
    elif startnumber==3:
        result = np.random.choice(State, p=probabilities[2])
    elif startnumber==4:
        result = np.random.choice(State, p=probabilities[3])
    elif startnumber==5:
        result = np.random.choice(State, p=probabilities[4])
    elif startnumber==6:
        result = np.random.choice(State, p=probabilities[5])
    return result

print (dice_roll_markov_chain(5))