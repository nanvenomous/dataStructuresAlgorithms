import pytest
from ..reconstruct_itinerary import ReconstructItinerary

class mock:
    class simple:
        inputs = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        outputs = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    class multiple_choice:
        inputs = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        outputs = ["JFK","ATL","JFK","SFO","ATL","SFO"]

    class failed:
        inputs = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        outputs = ["JFK","NRT","JFK","KUL"]

class TestReconstructItinerary:

    @classmethod
    def setup_class(cls):
        cls.subject = ReconstructItinerary()

    def assert_flight_priority(self, inputs, outputs):
        assert self.subject.findItinerary(inputs) == outputs

    def test_solves_simple_itinerary(self):
        self.assert_flight_priority(mock.simple.inputs, mock.simple.outputs)

    def test_solves_multiple_choice_itinerary(self):
        self.assert_flight_priority(mock.multiple_choice.inputs, mock.multiple_choice.outputs)

    def test_solves_failed_itinerary(self):
        self.assert_flight_priority(mock.failed.inputs, mock.failed.outputs)

    @classmethod
    def teardown_class(cls): pass

# @pytest.mark.skip()