from typing import List
from enum import Enum, auto
from collections import deque

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()

class MoveQuality(Enum):
    INVALID = auto()
    WALL = auto()
    VALID = auto()

# direction: (idx, toAdd)
dirmap = {
        Direction.UP: (0, -1),
        Direction.DOWN: (0, 1),
        Direction.RIGHT: (1, 1),
        Direction.LEFT: (1, -1),
        }

class Solution:
    def __init__(self):
        self.grid = [[]]
        self.height = None
        self.width = None
        self.answer = -1
        self.toSearch = deque()
        self.been = []

    def _grid_at(self, pos):
        return self.grid[pos[0]][pos[1]]

    def _get_pos(self, pos, direction):
        idx, toAdd = dirmap[direction]
        new = [p for p in pos]
        new[idx] += toAdd
        return new

    def _valid_move(self, newPos, demols):
        if (newPos, demols) in self.been: return MoveQuality.INVALID
        if newPos[0] < 0: return MoveQuality.INVALID
        if newPos[0] >= self.height: return MoveQuality.INVALID
        if newPos[1] < 0: return MoveQuality.INVALID
        if newPos[1] >= self.width: return MoveQuality.INVALID
        if self._grid_at(newPos) == 1: return MoveQuality.WALL
        return MoveQuality.VALID

    def _safe_append(self, pos, nmoves, demols, direction):
        nxt = self._get_pos(pos, direction)
        mq = self._valid_move(nxt, demols)
        if mq == MoveQuality.VALID:
            self.toSearch.append((nxt, nmoves + 1, demols))
        if demols and mq == MoveQuality.WALL:
            self.toSearch.append((nxt, nmoves + 1, demols - 1))

    def _add_next_moves(self, pos, nmoves, demols):
        self.been.append((pos, demols))
        if pos == [0, 0]:
            self.answer = nmoves

        for direct in list(Direction):
            self._safe_append(pos, nmoves, demols, direct)

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        pos = [self.height - 1, self.width - 1]
        self.toSearch.append((pos, 0, k))
        while self.answer == -1 and self.toSearch:
            nxtSearch = self.toSearch.popleft()
            self._add_next_moves(*nxtSearch)

        return self.answer
