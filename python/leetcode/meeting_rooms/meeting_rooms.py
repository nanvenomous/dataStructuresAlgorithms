from typing import List

class MeetingRooms:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        self.intervals: List[List[int]] = intervals
        self.groups: List[List[List[int]]] = []
        belongs: bool = False
        self.sort_by_first_interval_element()
        if not self.intervals: return 0
        itvl: List[int] = self.intervals.pop()
        self.groups.append([itvl])
        for _ in range(len(self.intervals)):
            itvl = self.intervals.pop()
            belongs = False
            for group in self.groups:
                high_lim = group[-1][-1]
                if itvl[0] >= high_lim:
                    group.append(itvl)
                    belongs = True
                    break
            if not belongs:
                self.groups.append([itvl])
        return len(self.groups)

    def sort_by_first_interval_element(self) -> None:
        def _get_key_first_element(elem: List[int]) -> int:
            return elem[0]
        self.intervals.sort(reverse=True, key=_get_key_first_element)