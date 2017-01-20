import random

class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, deltaX, deltaY):
		return Location(self.x + deltaX, self.y + deltaY)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def distFrom(self, other):
		ox = other.x
		oy = other.y
		xDist = self.x - ox
		yDist = self.y - oy

		# pythagorean theorem
		return (xDist**2 + yDist**2)**0.5

	def __str__(self):
		return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
	def __init__(self):
		# mapping from drunks to locations
		self.drunks = {}

	def addDrunk(self, drunk, loc):
		if drunk in self.drunks:
			raise ValueError('Duplicate drunk')
		else:
			# drunk has to be hashable!
			self.drunks[drunk] = loc

	def getLoc(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')

		return self.drunks[drunk]

	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		
		xDist, yDist = drunk.takeStep()
		currentLocation = self.drunks[drunk]

		# use move method of Location to get new location
		self.drunks[drunk] = currentLocation.move(xDist, yDist)

# used as a base class to be inherited
class Drunk(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'This drunk is named' + self.name

class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(stepChoices)

class ColdDrunk(Drunk):
	def takeStep(self):
		# biased walk
		stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(stepChoices)


def walk(f, d, numSteps):
	start = f.getLoc(d)

	for s in range(numSteps):
		f.moveDrunk(d)

	return start.distFrom(f.getLoc(d))

# dClass is of type `class`
def simWalks(numSteps, numTrials, dClass):
	Homer = dClass('h')
	origin = Location(0, 0)
	distances = []

	for t in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distances.append(round(walk(f, Homer, numSteps), 1))

	return distances

def drunkTest(walkLengths, numTrials, dClass):
	for numSteps in walkLengths:
		distances = simWalks(numSteps, numTrials, dClass)

		print(dClass.__name__, 'random walk of', numSteps, 'steps')

		print(' Mean =', round(sum(distances)/len(distances), 4))

		print(' Max =', max(distances), 'Min =', min(distances))

def simAll(drunkKinds, walkLengths, numTrials):
	for dClass in drunkKinds:
		drunkTest(walkLengths, numTrials, dClass)

simAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)
#drunkTest((10, 100, 1000, 10000, 100000, 1000000), 100, UsualDrunk)
#drunkTest((1, 2, 3, 4), 100, UsualDrunk)