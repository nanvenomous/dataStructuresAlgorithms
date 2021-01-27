from typing import List

class ContainerWithWater:
    def __init__(self):
        self.curMax = 0
        self.end = 0
        self.heights = []

    def maxArea(self, height: List[int]) -> int:
        self.heights = height
        self.end = len(height)
        while self.end > 1:
            self.singleArea()
            self.end -= 1
        return self.curMax

    def singleArea(self):
        eff_end = self.end - 1
        for i in range(eff_end):
            dist = eff_end - i
            height = min(self.heights[i], self.heights[eff_end])
            area = dist * height
            self.curMax = max(self.curMax, area)