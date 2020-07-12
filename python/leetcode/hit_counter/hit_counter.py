from collections import deque

class HitCounter:

    def __init__(self):
        """
        using a deque for it's first in last out nature
        """
        self.counter = deque()
        self.limit = 5*60 # 5 minutes or 300 seconds

    def remove_unecessary_counts(self, timestamp: int) -> None:
        while self.counter and timestamp - self.counter[0] >= self.limit:
            self.counter.popleft()


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.counter.append(timestamp)
        self.remove_unecessary_counts(timestamp)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.remove_unecessary_counts(timestamp)
        return len(self.counter)

    def clear(self) -> None:
        self.counter.clear()