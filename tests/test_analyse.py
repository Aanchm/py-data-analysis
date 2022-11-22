import unittest
import sys
import os.path
from pathlib import Path
import pandas as pd
import numpy as np

sys.path.append(rf"{Path(__file__).parent.parent}\src")
import analyse_data as an


class test_calculate_rms(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame({'A': [1, -2, 3], 'B': ["B1", "B2", "B3"]})
        
    def test_good_input_returns_correct_rms(self):
        actual_rms = an.calculate_rms(self.df, "A")
        expected_rms = np.sqrt(14/3)
        self.assertEqual(actual_rms, expected_rms, "rms vals not equal")

    def test_non_existent_column_returns_None(self):
        actual_rms = an.calculate_rms(self.df, "D")
        expected_rms = None
        self.assertEqual(actual_rms, expected_rms, "rms vals not equal")

    def test_non_integer_column_returns_None(self):
        actual_rms = an.calculate_rms(self.df, "B")
        expected_rms = None
        self.assertEqual(actual_rms, expected_rms, "rms vals not equal")


class test_get_stats_on_col(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame({'A': [1, -2, 3], 'B': ["B1", "B2", "B3"]})
        
        
    def test_good_input_returns_correct_stats(self):
        actual_stddev, actual_stderr = an.get_stats_on_col(self.df, "A")
        expected_stddev = 2.516611478
        expected_stderr = expected_stddev/np.sqrt(3)
        self.assertAlmostEqual(actual_stddev, expected_stddev, 7, "std_dev not equal")
        self.assertAlmostEqual(actual_stderr, expected_stderr, 7, "std_err not equal")


    def test_non_existent_column_returns_None(self):
        actual_stddev, actual_stderr = an.get_stats_on_col(self.df, "D")
        expected_stddev = None
        expected_stderr = None
        self.assertAlmostEqual(actual_stddev, expected_stddev, 7, "std_dev not equal")
        self.assertAlmostEqual(actual_stderr, expected_stderr, 7, "std_err not equal")


    def test_non_integer_column_returns_None(self):
        actual_stddev, actual_stderr = an.get_stats_on_col(self.df, "B")
        expected_stddev = None
        expected_stderr = None
        self.assertAlmostEqual(actual_stddev, expected_stddev, 7, "std_dev not equal")
        self.assertAlmostEqual(actual_stderr, expected_stderr, 7, "std_err not equal")


if __name__ == '__main__':
    unittest.main()