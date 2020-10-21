import pytest
from ..bus_stops import BusStops
from unittest.mock import call, Mock
from mock import patch

class mocks:
    ex1 = {
        1: ['a', 'b', 'c', 'd'],
        2: ['e', 'c', 'f', 'g'],
        3: ['d', 'h', 'k'],
        4: ['j', 'l', 'm', 'n'],
        5: ['z', 'n']
        }
    ex2 = {
        1: ['a', 'b'],
        2: ['b', 'c'],
        3: ['c', 'd']
    }
    simplest = {
        1: ['a', 'b'],
        2: ['b', 'c'],
    }

    multi_start = {
        1: ['a', 'b', 'u'],
        2: ['b', 'c', 'z'],
        3: ['z', 'x'],
        4: ['y', 'x', 'w'],
        5: ['y', 't', 'u']
    }

    multi_direction = {
        1: ['a', 'b'],
        2: ['b', 'c', 'd'],
        3: ['d', 'z'],
        4: ['z', 'a', 'x'],
    }

class TestBusStops:
    @classmethod
    def setup_class(cls): pass

    @classmethod
    def setup_method(cls):
        cls.subject = BusStops()

    def test_returns_from_correct_starting_point(self):
        ans = self.subject.numberBusses(mocks.multi_start, ('z', 'u'))
        assert len(self.subject.possibleAnswers) == 2
        assert 2 == ans

    def test_ex2_double_transfer(self):
        ans = self.subject.numberBusses(mocks.ex2, ('a', 'd'))
        assert 3 == ans

    def test_single_transfer(self):
        ans = self.subject.numberBusses(mocks.simplest, ('a', 'c'))
        assert 2 == ans

    #---------------------------------------------------------------------
    # findRoute
    def assert_shortest_route(self, schedule, bus, end, numVisits):
        self.subject.schedule = schedule
        self.subject.end = end
        self.subject.getBusTransferGraph()

        assert numVisits == self.subject.findRoute(bus)

    def test_finds_it_in_current_stops_when_also_elsewhere(self):
        self.assert_shortest_route(mocks.ex1, 1, 'd', 1)

    def test_multi_direction(self):
        self.assert_shortest_route(mocks.multi_direction, 2, 'a', 2)
        self.assert_shortest_route(mocks.multi_direction, 2, 'x', 3)

    def test_ex2(self):
        self.assert_shortest_route(mocks.ex2, 1, 'd', 3)
        
    def test_simplest(self):
        self.assert_shortest_route(mocks.simplest, 1, 'c', 2)

    #---------------------------------------------------------------------
    # getBusTransferGraph
    def test_get_transfers(self):
        self.subject.schedule = mocks.ex1
        self.subject.getBusTransferGraph()
        transfer_3 = self.subject.transfers[3]
        assert 1 in transfer_3
        assert 2 not in transfer_3
        assert 4 not in transfer_3
        assert 5 not in transfer_3

    #---------------------------------------------------------------------
    # getStartingPoints
    def get_starting_points(self, start, end, possible_starts, mock_findRoute):
        self.subject.start = start
        self.subject.end = end
        self.subject.schedule = mocks.ex1
        self.subject.getStartingPoints()
        assert mock_findRoute.call_count == possible_starts

    @patch.object(BusStops, 'findRoute')
    def test_get_starting_points_a(self, mock_findRoute):
        self.get_starting_points('a', 'e', 1, mock_findRoute)

    @patch.object(BusStops, 'findRoute')
    def test_get_starting_points_d(self, mock_findRoute):
        self.get_starting_points('d', 'e', 2, mock_findRoute)

    @classmethod
    def teardown_class(cls):
        cls.subject = BusStops()

# @pytest.mark.skip()
