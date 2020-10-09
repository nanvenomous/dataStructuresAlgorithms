import pytest
# for output
# pytest -vs
# for no output
# pytest -v

from ..fizzbuz import fizzBuzz, handle_individual_number

mock_15 = [
    1,
    2,
    'Fizz',
    4,
    'Buzz',
    'Fizz',
    7,
    8,
    'Fizz',
    'Buzz',
    11,
    'Fizz',
    13,
    14,
    'FizzBuzz',
    ]

class TestFizzBuzz:
	# @classmethod
	# def setup_method(cls):
	# 	cls.subject = fizzBuzz

    def test_individual(self):
        ex_li = []
        handle_individual_number(3, ex_li)
        print()
        print(ex_li)

    def test_returns_simple_fizz_buzz_list(self):
        assert mock_15 == fizzBuzz(15)

# @pytest.mark.skip()
