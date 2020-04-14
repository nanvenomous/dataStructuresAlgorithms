import pytest
import numpy as np

from ..buy_sell import MaxProfit

class TestBuySell:

    @classmethod
    def setup_class(cls):
        cls.subject = MaxProfit()
        cls.mock_sporadic = [7, 1, 5, 3, 6, 4]
        cls.mock_climb = [1, 2, 3, 4, 5]
        cls.mock_descent = [7, 6, 4, 3, 1]

    @classmethod
    def setup_method(cls): pass

    def test_returns_correct_sporadic(self):
        self.subject.maxProfit(self.mock_sporadic)
        assert self.subject.profit == [4, 3]
        assert 7 == self.subject.maxProfit(self.mock_sporadic)

    def test_returns_correct_climb(self):
        assert 4 == self.subject.maxProfit(self.mock_climb)

    def test_returns_correct_descent(self):
        assert 0 == self.subject.maxProfit(self.mock_descent)

    def test_interpolates(self):
        self.subject.y = [1, 2, 3]
        self.subject._get_indicators()
        np.testing.assert_array_equal(self.subject.y_interp, np.array([1, 1.5, 2, 2.5, 3]))
        np.testing.assert_array_equal(self.subject.indicators, np.array([1., 1.]))


@pytest.mark.skip()
class TestBuySellPlotting:

    @classmethod
    def setup_class(cls):
        import matplotlib.pyplot as plt
        cls.plt = plt

        cls.simple_input = [7, 1, 5, 3, 6, 4]

    @classmethod
    def setup_method(cls): pass

    def test_plot_values(self):
        lastIndex = len(self.simple_input) - 1
        x = np.linspace(0, lastIndex, lastIndex + 1)
        x_int = np.linspace(0, lastIndex, (lastIndex*2) + 1)
        y_int = np.interp(x_int, x, self.simple_input)
        self.plt.figure()
        self.plt.title('simple input')
        self.plt.xlabel('time [days]')
        self.plt.ylabel('dollars [$]')
        self.plt.plot(x_int, y_int, label='data')
        single_deriv = np.gradient(y_int, x_int)
        self.plt.scatter(x_int, single_deriv, label='derivative')
        # double_deriv = np.gradient(single_deriv, x_int)
        # self.plt.scatter(x_int, double_deriv, label='d2')
        self.plt.legend()

    @classmethod
    def teardown_class(cls):
        cls.plt.show()