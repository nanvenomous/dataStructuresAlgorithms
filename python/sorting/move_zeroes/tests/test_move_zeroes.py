import pytest
from ..move_zeroes import MoveZeroesStillTooSlow, MoveZeroes
from random import shuffle

class TestMoveZeroes:

    @classmethod
    def setup_class(cls):
        cls.subject = MoveZeroes()

    @classmethod
    def setup_method(cls):
        cls.subject.num_i.queue.clear()
        cls.subject.zero_i.queue.clear()
        cls.subject.ni = 0
        cls.subject.zi = 0
        cls.subject.zn = 0

        cls.mock_fewer_zeroes = [0, 1, 0, 3, 12]
        cls.mock_fewer_zeroes_output = [1, 3, 12, 0, 0]
        cls.mock_with_negatives = [271, -337, 0, 0, 5, -1000]
        cls.mock_with_negatives_output = [271, -337, 5, -1000, 0, 0]
        cls.mock_with_more_zeroes = [0, 1, 0, 0, -2]
        cls.mock_many_numbers = [
            -1278640323, 349172856, 1873509219, 2086212774, 0,
            -1001344505, -61069976, 746705870, -173131555, -1898820175,
            802998965, -916055673, 344084770, -1664334387, -1886907515,
            171107295, -2065649057, -1628881728, -1900147601, -342880452,
            -2037018488, -104769833, 0, 0, 374941067,
            536619007, -298730590, -1594869648, 1855390876, 904830187,
            -809158725, -1923547142, 1340100626, 953054962, 1195315949,
            0, 1281604841, 58893147, 2109018765, -928102085,
            -348541385, 1222161829, -319162010, -1229679355, 635148638,
            1343064576, 1235762604, 808863719, -1399893584, 262412042,
            852755753, 0]

    def test_randomized_moves_zeroes(self):
        # brute forcing to find edge cases
        print()
        # to_test = self.mock_with_more_zeroes
        # num_zeroes = 3
        to_test = self.mock_many_numbers
        num_zeroes = 5
        for _ in range(100):
            shuffle(to_test)
            orig = to_test.copy()
            print(orig)
            self.subject.moveZeroes(to_test)
            print(to_test)
            print()
            for i in range(num_zeroes):
                assert 0 == to_test[(i + 1) * -1]
            i = 0
            for num in to_test[:-1*num_zeroes]:
                while orig[i] == 0: i += 1
                assert num == orig[i]
                i += 1

@pytest.mark.skip()
class TestMoveZeroesStillTooSlow:

    @classmethod
    def setup_class(cls):
        cls.subject = MoveZeroesStillTooSlow()

    @classmethod
    def setup_method(cls):
        cls.subject.num_i.queue.clear()
        cls.subject.zero_i.queue.clear()
        cls.subject.ni = 0
        cls.subject.zi = 0
        cls.subject.zn = 0

        cls.mock_fewer_zeroes = [0, 1, 0, 3, 12]
        cls.mock_fewer_zeroes_output = [1, 3, 12, 0, 0]
        cls.mock_with_negatives = [271, -337, 0, 0, 5, -1000]
        cls.mock_with_negatives_output = [271, -337, 5, -1000, 0, 0]
        cls.mock_with_more_zeroes = [0, 1, 0, 0, -2]
        cls.mock_many_numbers = [
            -1278640323, 349172856, 1873509219, 2086212774, 0,
            -1001344505, -61069976, 746705870, -173131555, -1898820175,
            802998965, -916055673, 344084770, -1664334387, -1886907515,
            171107295, -2065649057, -1628881728, -1900147601, -342880452,
            -2037018488, -104769833, 0, 0, 374941067,
            536619007, -298730590, -1594869648, 1855390876, 904830187,
            -809158725, -1923547142, 1340100626, 953054962, 1195315949,
            0, 1281604841, 58893147, 2109018765, -928102085,
            -348541385, 1222161829, -319162010, -1229679355, 635148638,
            1343064576, 1235762604, 808863719, -1399893584, 262412042,
            852755753, 0]

    # @pytest.mark.skip()
    def test_randomized_moves_zeroes(self):
        # brute forcing to find edge cases
        print()
        # to_test = self.mock_with_more_zeroes
        # num_zeroes = 3
        to_test = self.mock_many_numbers
        num_zeroes = 5
        for _ in range(100):
            shuffle(to_test)
            orig = to_test.copy()
            print(orig)
            self.subject.moveZeroes(to_test)
            print(to_test)
            print()
            for i in range(num_zeroes):
                assert 0 == to_test[(i + 1) * -1]
            i = 0
            for num in to_test[:-1*num_zeroes]:
                while orig[i] == 0: i += 1
                assert num == orig[i]
                i += 1

    # @pytest.mark.skip()
    def test_moves_zeroes_with_negatives(self):
        self.subject.moveZeroes(self.mock_with_negatives)
        assert self.mock_with_negatives == self.mock_with_negatives_output

    # @pytest.mark.skip()
    def test_moves_fewer_zeroes(self):
        self.subject.moveZeroes(self.mock_fewer_zeroes)
        assert self.mock_fewer_zeroes == self.mock_fewer_zeroes_output

    def test_swaps_elements_by_indices(self):
        self.subject.nums = self.mock_fewer_zeroes
        self.subject.zi = 0
        self.subject.ni = 3
        self.subject._swap_positions()
        assert [3, 1, 0, 0, 12] == self.mock_fewer_zeroes

    def simple_example_setup(self):
        li = [-1, 0, 1, 0, 3, 7]
        self.subject.nums = li.copy()
        self.subject._get_indices()
        assert list(self.subject.num_i.queue) == [0, 2, 4, 5]
        assert list(self.subject.zero_i.queue) == [1, 3]

    def test_swaps_all(self):
        #      0  1  2  3  4  5
        self.simple_example_setup()
        # Iteration 1
        self.subject.zi = self.subject.zero_i.get()
        self.subject.zn = self.subject.zero_i.get()
        self.subject._swap_all_conditionally()
        assert self.subject.nums == [-1, 1, 3, 0, 7, 0]
        assert list(self.subject.num_i.queue) == [4]

        self.subject.zi = self.subject.zn
        self.subject._swap_all_conditionally()
        assert self.subject.nums == [-1, 1, 3, 7, 0, 0]
        assert list(self.subject.num_i.queue) == []

    def single_ni_iteration(self, nums_state, num_i_state):
        self.subject.ni = self.subject.num_i.get()
        self.subject._swap_conditionally()
        assert self.subject.nums == nums_state
        assert list(self.subject.num_i.queue) == num_i_state

    def test_swaps_if_conditions_are_met(self):
        #      0  1  2  3  4  5
        self.simple_example_setup()
        self.subject.num_i.put(None)
        # Iteration 1
        self.subject.zi = self.subject.zero_i.get()
        self.subject.zn = self.subject.zero_i.get()
        self.single_ni_iteration([-1, 0, 1, 0, 3, 7], [2, 4, 5, None])
        self.single_ni_iteration([-1, 1, 0, 0, 3, 7], [4, 5, None])
        self.single_ni_iteration([-1, 1, 3, 0, 0, 7], [5, None])
        self.single_ni_iteration([-1, 1, 3, 0, 7, 0], [None, 4])
        self.subject.zi = self.subject.zn
        # Iteration 2
        self.subject.num_i.get()
        self.subject.num_i.put(None)
        self.single_ni_iteration([-1, 1, 3, 7, 0, 0], [None])