import pytest
from ..decode_string import DecodeString

class mock:
    simple_input = '3[a]2[bc]'
    nested_input = '3[a2[c]]'
    single_and_double = '3[a]2[b4[F]c]'

class TestDecodeString:

    @classmethod
    def setup_class(cls):
        cls.subject = DecodeString()

    def test_simple_input(self):
        assert 'aaabcbc' == self.subject.decodeString(mock.simple_input)

    def test_nested_input(self):
        assert 'accaccacc' == self.subject.decodeString(mock.nested_input)

    @pytest.mark.skip()
    def test_single_and_double(self):
        assert 'aaabFFFFcbFFFFc' == self.subject.decodeString(mock.single_and_double)

    def test_decode_one_layer(self):
        print()
        self.subject.s = mock.single_and_double
        self.subject.decode_one_layer()
        print(self.subject.s)

    @classmethod
    def teardown_class(cls): pass

    # @pytest.mark.skip()