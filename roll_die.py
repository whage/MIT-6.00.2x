import random
import math

def rollDie():
	# returns a randomly chosen one with equal probability
	return random.choice([1,2,3,4,5,6,7])

def testRoll(n = 10):
	result = ''

	for i in range(n):
		result = result + str(rollDie())

	print(result)

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    return int(math.floor(random.randint(0, 99) / 2)) * 2

for i in range(20):
	print(genEven())