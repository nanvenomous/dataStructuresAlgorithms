import pytest
from unittest.mock import patch
from ..text_justification import TextJustification

class mocks:
    class one: 
        words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
        maxWidth = 16

class answers:
    one = [
            'This    is    an',
            'example  of text',
            'justification.  ',
            ]

class TestTextJustification:
    @classmethod
    def setup_method(cls):
        cls.subject = TextJustification()

    # def test_example(self):
    #     assert self.subject.fullJustify(mocks.one.words, mocks.one.maxWidth) == 0

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