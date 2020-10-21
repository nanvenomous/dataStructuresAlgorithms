# Question
City with a bus system:
Bus 1: stops a, b, c, d
Bus 2: stops e, c, f, g

Each route is bidirectional

Calculate the minimum # of buses someone needs to travel from one stop to another.

Example: D -> A (one bus)
Example: A -> G (two bus)


Input: Dictionary{bus number, [list of stops]}

(Start, stop)

1: [2, 4, 5]
2: [1, 3, 4]

# Proposed Solution
if in the current bus
else if bus has connections
	check all the connections
		check all the connections connections