from typing import List
from math import comb

class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if self.is_impossible(numCourses, len(prerequisites)): return False
        return True

    def is_impossible(self, numCourses, numPrerequisites):
        numPossibleCombinations = comb(numCourses, 2)
        print(numPossibleCombinations)
        return numPrerequisites > numPossibleCombinations
