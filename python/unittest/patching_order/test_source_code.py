import pytest
from mock import patch

from source_code import add_the_numbers

@patch('source_code.one')
class TestCase():

  @patch('source_code.two')
  def test_with_mock(self, mock_two, mock_one):
    mock_one.return_value = 3
    mock_two.return_value = 1
    assert 2 == add_the_numbers()

  def test_without_mock(self, mock_one):
    mock_one.return_value = 3
    assert 1 == add_the_numbers()