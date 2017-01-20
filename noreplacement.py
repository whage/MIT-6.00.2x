import random

#random.seed(0)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count = 0

    for i in range(numTrials):
        bag = [0,0,0,1,1,1]        
        
        for i in range(3):
            removeRandom(bag)

        if allItemsEqual(bag):
            count = count + 1

    return count / numTrials


def removeRandom(list):
    idx = random.randint(0, len(list) - 1)
    del list[idx]



#list = [0,0,0,1,1,1]
#removeRandom(list)
#print(list)

def allItemsEqual(list):
    first = list[0]
    i = 1

    while (i < len(list)) and (list[i] == first):
        i = i + 1

    return i == len(list)

#print(allItemsEqual([1,1,1,0,1,1,1,1]))
