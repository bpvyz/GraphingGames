import unittest
import os
import pandas as pd


class TestDataLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup that runs once before all tests"""
        cls.df = None
        try:
            from task import df
            cls.df = df
        except Exception as e:
            cls.import_error = str(e)

    def test_pandas_import(self):
        """Test if pandas library is installed"""
        try:
            import pandas as pd
            self.assertTrue(True, "Pandas is installed.")
        except ImportError:
            self.fail("Pandas is not installed.")

    def test_code_execution(self):
        """Test if the code runs without exceptions"""
        if not hasattr(self, 'df'):
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
        if hasattr(self, 'df'):
            try:
                self.assertIsNotNone(self.df, "DataFrame 'df' is None. Are you loading the proper .csv file?")
                self.assertIsInstance(self.df, pd.DataFrame, "Variable 'df' is not a pandas DataFrame")

                required_columns = {'platform', 'genre'}
                missing_columns = required_columns - set(self.df.columns)
                if missing_columns:
                    file_path = '../dataset.csv'
                    if os.path.exists(file_path):
                        try:
                            test_df = pd.read_csv(file_path)
                            actual_columns = set(test_df.columns)
                            if not required_columns.issubset(actual_columns):
                                self.fail(f"The CSV file is missing required columns: {missing_columns}.\n"
                                          f"Expected columns: {required_columns}\n"
                                          f"Found columns: {actual_columns}")
                            else:
                                self.fail(f"Required columns {missing_columns} exist in the CSV file but "
                                          f"are not present in your DataFrame. Check your data loading code.")
                        except Exception as e:
                            self.fail(f"File exists but contains wrong columns.\n"
                                      f"Missing required columns: {missing_columns}")
                    else:
                        self.fail(f"File not found and DataFrame is missing required columns: {missing_columns}")

            except AssertionError as e:
                file_path = '../dataset.csv'
                if not os.path.exists(file_path):
                    self.fail(f"File not found: {file_path}\nMake sure 'dataset.csv' is in the correct location")
                else:
                    self.fail(str(e))
        else:
            self.fail("Could not test DataFrame: Code execution failed")

    def test_file_location(self):
        """Test if the CSV file exists and can be read"""
        file_path = '../dataset.csv'
        if not os.path.exists(file_path):
            self.fail(f"File not found: {file_path}\nMake sure 'dataset.csv' is in the correct location")
        else:
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
