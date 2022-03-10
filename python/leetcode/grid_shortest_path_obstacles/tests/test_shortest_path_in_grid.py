from ..shortest_path_in_grid import Solution

class mocks:
    class one:
        grid = [
                [0,0,0],
                [1,1,0],
                [0,0,0],
                [0,1,1],
                [0,0,0]
                ]
        k = 1
        answer = 6

    class two:
        grid = [[0]]
        k = 1
        answer = 0

    class three:
        grid = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,0,1,1,1,1,1,1,1],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,0,1,1,1,1,1,1,1],
                [0,1,0,1,1,1,1,0,0,0],
                [0,1,0,0,0,0,0,0,1,0],
                [0,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,1,0]
                ]
        k = 1
        answer = 20


class TestSolution:
    @classmethod
    def setup_class(cls): pass

    @classmethod
    def setup_method(cls):
        cls.subject = Solution()

    def assert_passes_mock(self, mock):
        ans = self.subject.shortestPath(mock.grid, mock.k)
        assert ans == mock.answer

    def test_mock_one(self):
        self.assert_passes_mock(mocks.one)

    def test_mock_two(self):
        self.assert_passes_mock(mocks.two)

    def test_mock_three(self):
        self.assert_passes_mock(mocks.three)
