class Node:
	def __init__(self, value=None, children = []):
		self.value = value
		self. children = children

# 1 -> 3 -> 4
#  \
#   6
# return 2

# 1 -> 3 -> 4
#  \
#   2 -> 8 -> 9 -> 10
#    \
#     3 -> 4
# return 4

# if there are no children return 1
# else: 
    # for each child
        # make recursive call and get subtree max consec
        # use it to determine your return
# return 

class LongestConsecutive:
    def getLongestConsecutive(self, node):
        self.totMax = 1
        self.maxConsecutive(node)
        return self.totMax

    def isConsecutive(self, node, child):
        return child.value == node.value + 1

    def maxConsecutive(self, node):
        # if there are no children return 1
        if not node.children: return 1
        else: # there are children
            maxOfChildren = 1
            for child in node.children:
                # make recursive call and get subtree max consec
                subMax = self.maxConsecutive(child)

                # if is isConsecutive update max of all the children subtrees
                if self.isConsecutive(node, child):
                    maxOfChildren = max([subMax + 1, maxOfChildren])
        self.totMax = max([self.totMax, maxOfChildren])
        return maxOfChildren