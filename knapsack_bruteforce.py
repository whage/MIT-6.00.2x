def maxVal(toConsider, avail):
	if toConsider == [] or avail == 0:
		result = (0, ())
	elif toConsider[0].getUnits() > avail:
		result = maxVal(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits())
		withVal += nextItem.getValue()
		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
	if withVal > withoutVal:
		result = (withVal, withToTake + (nextItem,))
	else:
		result = (withoutVal, withoutToTake)
	return result