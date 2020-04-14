from typing import List
import numpy as np

class MaxProfit:
    def _get_indicators(self):
        end = len(self.y) - 1
        self.x = np.linspace(0, end, end + 1)
        self.x_interp = np.linspace(0, end, (end*2) + 1)
        self.y_interp = np.interp(self.x_interp, self.x, self.y)
        deriv = np.gradient(self.y_interp, self.x_interp)
        self.indicators = deriv[1::2]

    def _calculate_profit(self):
        for (i, ind) in enumerate(self.indicators):
            if self.st is None and ind > 0:
                print(i)
                self.st = i
            elif self.st is not None and ind < 0: self._add_to_profit(i)
        if self.st is not None: self._add_to_profit(-1)

    def _add_to_profit(self, end):
        print(self.st, end)
        self.profit.append(self.y[end] - self.y[self.st])
        self.st = None

    def maxProfit(self, prices: List[int]) -> int:
        self.profit = []
        self.y = prices
        self.st = None
        if len(self.y) == 1: return 0
        self._get_indicators()
        self._calculate_profit()
        return sum(self.profit)
        