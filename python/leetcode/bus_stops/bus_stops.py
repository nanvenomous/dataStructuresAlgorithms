from collections import deque

class BusStops:
    def __init__(self):
        self.start = None
        self.end = None
        self.schedule = {}
        self.transfers = {}
        self.checked_busses = []
        self.to_check = deque()
        self.possibleAnswers = []


    # TODO: handle 0 case
    def numberBusses(self, schedule, journey):
        self.start, self.end = journey
        self.schedule = schedule
        self.getBusTransferGraph()
        self.getStartingPoints()
        answers = [e for e in self.possibleAnswers if e]
        if answers: return min(answers)
        else: return None

    def getStartingPoints(self):
        # for each bus containing the start
        for bus, stops in self.schedule.items():
            if self.start in stops:
                # current bus checked & now get best of each starting point
                self.possibleAnswers.append(self.findRoute(bus))

    def addBusToCheck(self, bus, visits):
        self.to_check.appendleft((bus, visits))

    def findRoute(self, startBus):
        visits = 1
        self.checked_busses = [startBus]
        self.to_check.clear()
        self.addBusToCheck(startBus, visits)

        while self.to_check:
            # check next bus in queue
            bus, visits = self.to_check.pop()
            stops = self.schedule[bus]
            if self.end in stops: return visits
            visits += 1

            # add transfers to check if necessary
            possibleTransfers = self.transfers[bus]
            for transfer in possibleTransfers:
                if transfer not in self.checked_busses:
                    self.addBusToCheck(transfer, visits)
                    self.checked_busses.append(transfer)

    # TODO: this method can be extracted to a delegate
    def getBusTransferGraph(self):
        # TODO: add pickle transfer graph, this method should only be run once
        for curBus in self.schedule:
            self.transfers[curBus] = []
            for bus in self.schedule:
                if not curBus is bus:
                    curStops = self.schedule[curBus]
                    stops = self.schedule[bus]
                    if set.intersection(set(curStops), set(stops)):
                        self.transfers[curBus].append(bus)
