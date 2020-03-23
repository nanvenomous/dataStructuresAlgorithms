import pytest
import re
import os, sys

# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

current_directory = os.path.dirname(os.path.abspath(__file__))
current_file = os.path.join(current_directory, 'example.txt')

file = open(current_file, 'r')
mock_text = file.read()

mock_names = [
	'Mr. Schafer',
	'Mr Smith',
	'Ms Davis',
	'Mrs. Robinson',
	'Mr. T',
]

letters_at_beginning = ['a', 'A', 'H', 'g', 'M', 'M', 'M', 'M', 'M']

phone_numbers = [
	'321-555-4321',
	'123.555.1234',
	'800-555-1234',
	'900-555-1234',
]
eight_nine_hundred_numbers = [
	'800-555-1234',
	'900-555-1234',
]

mock_nums_and_lets = 's0 88ff3 .i0'
mock_word_letter = 's 0F3 .- _+'
one_at_beginning = 'one one two one two'


class TestRegEx:
	@staticmethod
	def reg_find_all(to_find, find_in):
		pattern = re.compile(to_find)
		matches = pattern.findall(find_in)
		return matches

	@staticmethod
	def reg_search(to_find, find_in):
		pattern = re.compile(to_find)
		matches = pattern.search(find_in)
		return matches

	def test_simple_match(self):
		matches = self.reg_find_all(r'abc', mock_text)
		assert ['abc'] == matches

	def test_period_matches_everything_except_newline(self):
		matches = self.reg_find_all(r'.', mock_text)
		assert r'\n' not in matches
		
	def test_matches_actual_period(self):
		matches = self.reg_find_all(r'\.', mock_text)
		number_of_periods_in_mock_text = 6
		assert matches == ['.' for _ in range(number_of_periods_in_mock_text)]

	def test_excaping_period_to_match_url(self):
		matches = self.reg_find_all(r'google\.com', mock_text)
		assert matches == ['google.com']

	def test_d_matches_digit_zero_to_nine(self):
		matches = self.reg_find_all(r'\d', mock_nums_and_lets)
		assert matches == ['0', '8', '8', '3', '0']

	def test_D_matches_anything_not_a_digit(self):
		matches = self.reg_find_all(r'\D', mock_nums_and_lets)
		assert matches == ['s', ' ', 'f', 'f', ' ', '.', 'i']

	def test_d_d_matches_two_digits(self):
		matches = self.reg_find_all(r'\d\d', mock_nums_and_lets)
		assert matches == ['88']

	def test_matches_a_word_character(self):
		matches = self.reg_find_all(r'\w', mock_word_letter)
		assert matches == ['s', '0', 'F', '3', '_']

	def test_matches_not_a_word_character(self):
		matches = self.reg_find_all(r'\W', mock_word_letter)
		assert matches == [' ', ' ', '.', '-', ' ', '+']

	def test_matches_all_whitespace(self):
		matches = self.reg_find_all(r'\s', 's \t0F3 .\n- _+')
		assert matches == [' ', '\t', ' ', '\n', ' ']

	def test_matches_non_whitespace(self):
		matches = self.reg_find_all(r'\S', 's \t0F3 .\n- _+')
		assert matches == ['s', '0', 'F', '3', '.', '-', '_', '+']

	def test_word_after_word_boundry(self):
		matches = self.reg_find_all(r'\bHa', mock_text)
		assert matches == ['Ha', 'Ha']

	def test_word_not_after_word_boundry(self):
		matches = self.reg_find_all(r'\BHa', mock_text)
		assert matches == ['Ha']

	def test_word_beginning_of_line(self):
		matches = self.reg_find_all(r'^one', one_at_beginning)
		assert matches == ['one']

	def test_word_at_end_of_line(self):
		matches = self.reg_find_all(r'two$', one_at_beginning)
		assert matches == ['two']

	def test_matches_phone_numbers(self):
		matches = self.reg_find_all(r'\d{3}[-.]\d{3}[-.]\d{4}', mock_text)
		assert matches == phone_numbers

	def test_matches_800_and_900_phone_numbers(self):
		matches = self.reg_find_all(r'[89]00[-.]\d{3}[-.]\d{4}', mock_text)
		assert matches == eight_nine_hundred_numbers

	def test_only_finds_a_at_beginning_of_file(self):
		matches = self.reg_find_all(r'^[a-zA-Z]', mock_text)
		assert matches == ['a']

	def test_negates_b_in_bat(self):
		matches = self.reg_find_all(r'[^b]at', mock_text)
		assert matches == ['mat', 'pat']
