import pytest
from ..hit_counter import HitCounter

class mocks:
    empty_the_array = {
        'actions': ["hit","hit","hit","getHits","getHits","getHits","getHits","getHits","hit","getHits"],
        'times': [2,3,4,300,301,302,303,304,501,600]
        }

class TestHitCounter:

    @classmethod
    def setup_class(cls):
        cls.subject = HitCounter()

    @classmethod
    def setup_method(cls):
        cls.subject.counter.clear()

    def run_tests(self, mocked_values):
        for act, time in zip(mocked_values['actions'], mocked_values['times']):
            method = getattr(self.subject, act)
            if act == 'hit':
                method(time)
            elif act == 'getHits':
                print(method(time))


    def test_empties_the_array(self):
        self.run_tests(mocks.empty_the_array)
        

    def test_base_case(self):
        self.subject.hit(1)

        self.subject.hit(2)

        self.subject.hit(3)

        assert 3 == self.subject.getHits(4)

        self.subject.hit(300)

        assert 4 == self.subject.getHits(300)

        assert 3 == self.subject.getHits(301)

    @classmethod
    def teardown_class(cls): pass

    # @pytest.mark.skip()