import pytest
from unittest.mock import patch
from ..text_justification import TextJustification

class mocks:
    class one: 
        words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
        maxWidth = 16
    class two:
        words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be']
        maxWidth = 16
    class three:
        words = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do']
        maxWidth = 20

class answers:
    one = [
            'This    is    an',
            'example  of text',
            'justification.  ',
            ]
    two = [
            'What   must   be',
            'acknowledgment  ',
            'shall be        ',
            ]
    three = [
            'Science  is  what we',
            'understand      well',
            'enough to explain to',
            'a  computer.  Art is',
            'everything  else  we',
            'do                  ',
            ]

class TestTextJustification:
    @classmethod
    def setup_method(cls):
        cls.subject = TextJustification()

    def assert_justifies_text(self, mock, ans):
        assert self.subject.fullJustify(mock.words, mock.maxWidth) == ans

    def test_mock_one(self):
        self.assert_justifies_text(mocks.one, answers.one)

    def test_mock_two(self):
        self.assert_justifies_text(mocks.two, answers.two)

    def test_mock_three(self):
        self.assert_justifies_text(mocks.three, answers.three)

    def test_get_line(self):
        self.subject.words = mocks.one.words
        self.subject.maxWidth = mocks.one.maxWidth
        ans = self.subject._getLine(
            s=0,
            e=3,
            curLineLen=10
        )
        assert ans == answers.one[0]

    @patch.object(TextJustification, '_getLine')
    def test_measure_line(self, getLineMock):
        self.subject.words = mocks.one.words
        self.subject.maxWidth = mocks.one.maxWidth
        self.subject._measureLine(s=0)
        getLineMock.assert_called_once_with(
            s=0,
            e=3,
            curLineLen=10
            )

    @classmethod
    def teardown_class(cls): pass

# @pytest.mark.skip()