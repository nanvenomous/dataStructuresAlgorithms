
def insideInterval(toCheck, interval, includeEdges=True):
	if (includeEdges):
		outOfBounds = (toCheck < interval[0], toCheck > interval[1])
	else:
		outOfBounds = (toCheck <= interval[0], toCheck >= interval[1])
	if any(outOfBounds):
		return False
	return True
