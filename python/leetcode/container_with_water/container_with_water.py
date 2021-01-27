from typing import List

class ContainerWithWater:
    def __init__(self):
        self.curMax = 0
        self.start = 0
        self.end = None
        self.heights = None

    def _checkSingleArea(self):
        dist = self.end - self.start
        height = min(self.heights[self.start], self.heights[self.end])
        area = dist * height
        self.curMax = max(self.curMax, area)

    def maxArea(self, height: List[int]) -> int:
        self.heights = height
        self.end = len(height) - 1
        while self.end != self.start:
            self._checkSingleArea()
            potStart = self.start + 1
            potEnd = self.end - 1
            endHeight = self.heights[self.end]
            startHeight = self.heights[self.start]
            if endHeight < startHeight:
                self.end = potEnd
            elif startHeight < endHeight:
                self.start = potStart
            else:
                if self.heights[potStart] < self.heights[potEnd]:
                    self.end = potEnd
                else:
                    self.start = potStart
        return self.curMax