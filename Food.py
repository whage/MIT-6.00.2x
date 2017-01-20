from __future__ import print_function

class Food(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.calories = w

	def getValue(self):
		return self.value

	def getCost(self):
		return self.calories

	def density(self):
		return self.getValue() / self.getCost()

	def __str__(self):
		return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
	menu = []

	for i in range(len(values)):
		f = Food(names[i], values[i], calories[i])
		menu.append(f)

	return menu

def greedy(items, maxCost, keyFunction):
	itemsCopy = sorted(items, key = keyFunction, reverse = True)

	result = []
	totalValue, totalCost = 0.0, 0.0

	for i in range(len(itemsCopy)):
		if (totalCost + itemsCopy[i].getCost()) <= maxCost:
			#print('picking ', itemsCopy[i])
			result.append(itemsCopy[i])
			totalCost += itemsCopy[i].getCost()
			totalValue += itemsCopy[i].getValue()

	return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
	taken, val = greedy(items, constraint, keyFunction)
	print('Total value of items taken =', val)

	for item in taken:
		print(' ', item)

def testGreedys(foods, maxUnits):
	print('Use greedy by value to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.getValue)
	print('\nUse greedy by density to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, lambda x: 1/x.getCost())
	print('\nUse greedy by cost to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 30, 50, 90, 79, 90, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = [Food(names[ind], values[ind], calories[ind]) for ind, i in enumerate(values)]

testGreedys(foods, 750)

#words = sorted("This is a test string from Andrew".split(), str.lower)
#f3 = lambda x,y: 'factor' if (x % y == 0) else 'not factor'
#print f3(28800000, 12);