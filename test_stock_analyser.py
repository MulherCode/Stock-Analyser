import unittest
from data_fetcher import get_stock_data
from plotter import plot_stock_data
import pandas as pd

class TestStockAnalyser(unittest.TestCase):

    def test_get_stock_data_valid_ticker(self):
        data = get_stock_data("AAPL", "2023-01-01", "2023-06-01")
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

    def test_get_stock_data_invalid_ticker(self):
        data = get_stock_data("INVALID", "2023-01-01", "2023-06-01")
        self.assertIsNone(data)

    def test_plot_stock_data(self):
        # Assuming plot_stock_data just displays a plot and doesn't return anything
        data = get_stock_data("AAPL", "2023-01-01", "2023-06-01")
        self.assertIsNotNone(data)
        # Plotting should not raise any exceptions
        try:
            plot_stock_data(data, "AAPL")
        except Exception as e:
            self.fail(f"plot_stock_data raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
