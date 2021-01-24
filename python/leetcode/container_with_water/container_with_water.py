from typing import List

class ContainerWithWater:
    def __init__(self):
        self.maxArea = 0
        self.end = 0
        self.heights = []

    def findArea(self, height: List[int]) -> int:
        self.heights = height
        self.end = len(height)
        while self.end > 1:
            self.singleArea()
            self.end -= 1

    def singleArea(self):
        eff_end = self.end - 1
        for i in range(eff_end):
            dist = eff_end - i
            height = min(self.heights[i], self.heights[eff_end])
            area = dist * height
            self.maxArea = max(self.maxArea, area)