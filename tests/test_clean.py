import unittest
import sys
import os.path
from pathlib import Path
import pandas as pd


#TODO tests against peaks method

sys.path.append(rf"{Path(__file__).parent.parent}\src")
import clean_data as cl 


class test_standardise_data_col(unittest.TestCase):

    def setUp(self) -> None:
       self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8], 'C': [9, 12, 15]})
       self.string_df = pd.DataFrame({'A': ["A1", "A2", "A3"], 'B': [4, 6, 8]})

    def test_good_input_returns_normalised(self):
        actual_df = cl.standardise_data_col(self.df, "B").to_string()
        expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [0, 2, 4], 'C': [9, 12, 15]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_non_existent_col_returns_same_df(self):
        actual_df = cl.standardise_data_col(self.df, "D").to_string()
        expected_df = (self.df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_not_integers_returns_same_df(self):
        actual_df = cl.standardise_data_col(self.string_df, "A").to_string()
        expected_df = (self.string_df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")

    

class test_normalise_data_col(unittest.TestCase):

    def setUp(self) -> None:
        self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8], 'C': [9, 12, 15]})
        self.string_df = pd.DataFrame({'A': ["A1", "A2", "A3"], 'B': [4, 6, 8]})


    def test_good_input_returns_normalised(self):
        actual_df = cl.normalise_data_col(self.df, "B").to_string()
        expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [-2.0, 0.0, 2.0], 'C': [9, 12, 15]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_non_existent_col_returns_same_df(self):
        actual_df = cl.normalise_data_col(self.df, "D").to_string()
        expected_df = (self.df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_not_integers_returns_same_df(self):
        actual_df = cl.normalise_data_col(self.string_df, "A").to_string()
        expected_df = (self.string_df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


class test_filter_data_by_col_vals(unittest.TestCase):
    def setUp(self) -> None:
       self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8], 'C': [9, 12, 15]})
    

    def test_good_input_returns_correct_df(self):
        actual_df = cl.filter_data_by_col_vals(self.df, "A", [2, 3]).to_string()
        expected_df = pd.DataFrame({'A': [2, 3], 'B': [6, 8], 'C': [12, 15]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_non_existent_col_returns_same_df(self):
        actual_df = cl.filter_data_by_col_vals(self.df, "D", [3]).to_string()
        expected_df = (self.df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_no_val_returns_empty_df(self):
        actual_df = cl.filter_data_by_col_vals(self.df, "A", [6]).to_string()
        expected_df = pd.DataFrame({'A': [], 'B': [], 'C': []}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


class test_select_data_columns(unittest.TestCase):
    def setUp(self) -> None:
       self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8], 'C': [9, 12, 15]})
    

    def test_good_input_returns_correct_df(self):
        actual_df = cl.select_data_columns(self.df, ["A", "C"]).to_string()
        expected_df = pd.DataFrame({'A': [1, 2, 3], 'C': [9, 12, 15]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_non_existent_col_returns_correct_df(self):
        actual_df = cl.select_data_columns(self.df, ["A", "D"]).to_string()
        expected_df = pd.DataFrame({'A': [1, 2, 3]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


class test_get_data_with_col_greater_than_val(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8], 'C': [9, 12, 15]})
        self.string_df = pd.DataFrame({'A': ["A1", "A2", "A3"], 'B': [4, 6, 8]})


    def test_good_input_returns_normalised(self):
        actual_df = cl.get_data_with_col_greater_than_val(self.df, col="B", val=6).to_string()
        expected_df = pd.DataFrame({'A': [3], 'B': [8], 'C': [15]}).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_bad_col_returns_same_df(self):
        actual_df = cl.get_data_with_col_greater_than_val(self.df, col="D", val=5).to_string()
        expected_df = (self.df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


    def test_not_integers_returns_same_df(self):
        actual_df = cl.standardise_data_col(self.string_df, "A").to_string()
        expected_df = (self.string_df).to_string()
        self.assertEqual(actual_df, expected_df, "dataframes not equal")


if __name__ == '__main__':
    unittest.main()