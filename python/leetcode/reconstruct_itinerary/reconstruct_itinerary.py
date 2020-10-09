# https://leetcode.com/problems/reconstruct-itinerary/submissions/
from typing import List
from collections import defaultdict
from queue import PriorityQueue

class ReconstructItinerary():
    def findItinerary(self, tickets: List[List[str]], root='JFK') -> List[str]:
        self.map = defaultdict(lambda: PriorityQueue())
        self.flight_list = [root]
        self.conver_to_map(tickets)
        self.get_flight_list()
        return self.flight_list

    def conver_to_map(self, tickets):
        for from_airport, to_airport in tickets:
            self.map[from_airport].put(to_airport)

    def get_flight_list(self):
        next_que = self.map[self.flight_list[0]]
        while not next_que.empty():
            next_airport = next_que.get()
            self.flight_list.append(next_airport)
            next_que = self.map[next_airport]
