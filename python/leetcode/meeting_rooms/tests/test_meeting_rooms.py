import pytest
from ..meeting_rooms import MeetingRooms

class TestMeetingRooms:

	@classmethod
	def setup_method(cls):
		cls.subject = MeetingRooms()
		cls.mock_meetings = [[4, 12], [2, 4], [5, 10], [3, 5], [1, 3]]
		cls.mock_long_span = [[5, 10], [0, 30], [15, 20]]

	def test_sorts_by_first_element(self):
		self.subject.intervals = self.mock_meetings
		self.subject.sort_by_first_interval_element()
		assert self.subject.intervals == [[5, 10], [4, 12], [3, 5], [2, 4], [1, 3]]

	def test_correct_number_of_groups(self):
		ans = self.subject.minMeetingRooms(self.mock_meetings)
		assert ans == 2

	def test_correct_groups_long_span(self):
		ans = self.subject.minMeetingRooms(self.mock_long_span)
		assert ans == 2

	# @pytest.mark.skip()