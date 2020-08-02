
import pytest
from ..course_schedule import CourseSchedule


class TestCourseSchedule:
	@classmethod
	def setup_method(cls):
		cls.subject = CourseSchedule()

	def test_combinations_of_4_possibility(self):
		assert False == self.subject.is_impossible(4, 6)
		assert True == self.subject.is_impossible(4, 7)

	def test_combinations_of_3_possibility(self):
		assert False == self.subject.is_impossible(3, 3)
		assert True == self.subject.is_impossible(3, 4)

# @pytest.mark.skip()