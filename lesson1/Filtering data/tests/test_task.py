import unittest
import os
import pandas as pd


class TestDataProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup that runs once before all tests"""
        cls.df = None
        cls.filtered_df = None
        cls.filter_list = None
        try:
            from task import df, filtered_df, filter_list
            cls.df = df
            cls.filtered_df = filtered_df
            cls.filter_list = filter_list
        except Exception as e:
            cls.import_error = str(e)

    def test_pandas_import(self):
        try:
            import pandas as pd
            self.assertTrue(True, "Pandas is installed.")
        except ImportError:
            self.fail("Pandas is not installed.")

    def test_code_execution(self):
        if not hasattr(self, 'df') or not hasattr(self, 'filtered_df'):
            # If FileNotFoundError, check file location first
            if "No such file or directory" in getattr(self, 'import_error', ''):
                file_path = '../dataset.csv'
                if not os.path.exists(file_path):
                    self.fail(f"File not found: {file_path}\nMake sure 'dataset.csv' is in the correct location")
                else:
                    self.fail(f"File exists but couldn't be loaded. Check your file path in the code.")
            else:
                self.fail(f"Code execution failed: {getattr(self, 'import_error', 'Unknown error')}")

    def test_df_creation(self):
        """Test initial DataFrame creation"""
        if not hasattr(self, 'df'):
            self.fail("DataFrame 'df' not found. Did you create it?")

        self.assertIsNotNone(self.df, "DataFrame 'df' is None. Are you loading the proper .csv file?")
        self.assertIsInstance(self.df, pd.DataFrame, "Variable 'df' is not a pandas DataFrame")

        required_columns = {'platform', 'genre'}
        missing_columns = required_columns - set(self.df.columns)
        if missing_columns:
            self.fail(f"The DataFrame is missing required columns: {missing_columns}")

    def test_filtered_df_creation(self):
        """Test filtered DataFrame creation"""
        if not hasattr(self, 'filtered_df'):
            self.fail("filtered_df not found. Did you create it?")

        self.assertIsNotNone(self.filtered_df, "filtered_df is None")
        self.assertIsInstance(self.filtered_df, pd.DataFrame, "filtered_df is not a pandas DataFrame")

        expected_columns = {'platform', 'genre'}
        actual_columns = set(self.filtered_df.columns)
        if actual_columns != expected_columns:
            self.fail(f"filtered_df has wrong columns.\nExpected: {expected_columns}\nGot: {actual_columns}")

        allowed_platforms = set(self.filter_list)  # Use the filter_list defined in setUpClass
        actual_platforms = set(self.filtered_df['platform'].unique())
        invalid_platforms = actual_platforms - allowed_platforms

        if invalid_platforms:
            self.fail(f"filtered_df contains invalid platforms: {invalid_platforms}\n"
                      f"Only these platforms should be included: {allowed_platforms}")

        # Check if empty
        if self.filtered_df.empty:
            self.fail("filtered_df is empty. Check your filtering condition.")

    def test_filter_list(self):
        """Test if filter_list has the correct values"""
        expected_filter_list = {'PS4', 'XOne', 'PC', 'WiiU'}
        actual_filter_list = set(self.filter_list)  # Get actual filter_list from setUpClass
        self.assertEqual(actual_filter_list, expected_filter_list,
                         msg=f"filter_list should be {expected_filter_list} but got {actual_filter_list}")

    def test_filtered_df_comparison(self):
        """Compare filtered_df with student's expected filtered_df"""
        expected_filtered_df = self.df[self.df['platform'].isin(self.filter_list)][['platform', 'genre']]

        pd.testing.assert_frame_equal(self.filtered_df.reset_index(drop=True),
                                      expected_filtered_df.reset_index(drop=True),
                                      check_dtype=True, obj='Filtered DataFrame and expected DataFrame')

    def test_file_location(self):
        """Test if the file exists in the correct location"""
        file_path = '../dataset.csv'
        if not os.path.exists(file_path):
            self.fail(f"File not found: {file_path}\nMake sure 'dataset.csv' is in the correct location")

        try:
            test_df = pd.read_csv(file_path)
            required_columns = {'platform', 'genre'}
            missing_columns = required_columns - set(test_df.columns)
            if missing_columns:
                self.fail(f"The CSV file is missing required columns: {missing_columns}.\n"
                          f"Expected columns: {required_columns}\n"
                          f"Found columns: {set(test_df.columns)}")
        except Exception as e:
            self.fail(f"File exists but couldn't be read as CSV: {str(e)}")

    def test_proper_dataframe_loaded(self):
        """Test if the proper DataFrame is loaded and compare with the CSV data"""
        if hasattr(self, 'df'):
            file_path = '../dataset.csv'
            if os.path.exists(file_path):
                expected_df = pd.read_csv(file_path)

                pd.testing.assert_frame_equal(self.df.reset_index(drop=True), expected_df.reset_index(drop=True),
                                              check_dtype=True,
                                              obj='Loaded DataFrame and expected DataFrame')

            else:
                self.fail(f"File not found: {file_path}")


if __name__ == "__main__":
    unittest.main()
