import unittest
import os
import pandas as pd
from unittest.mock import patch
import matplotlib.pyplot as plt


class TestDataProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup that runs once before all tests"""
        cls.df = None
        cls.filtered_df = None
        cls.genre_counts = None
        cls.filter_list = ['PS4', 'XOne', 'PC', 'WiiU']

        # Correct the filename and check path
        file_path = '../dataset.csv'  # Make sure this is correct

        # Use os.path.abspath to print the absolute path for clarity
        absolute_path = os.path.abspath(file_path)
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(
                f"File not found: {absolute_path}\nMake sure 'dataset.csv' is in the correct location")

        try:
            from task import df, filtered_df, filter_list, genre_counts
            cls.df = df
            cls.filtered_df = filtered_df
            cls.filter_list = filter_list
            cls.genre_counts = genre_counts

            # Ensure the DataFrame is loaded correctly
            assert cls.df is not None, "DataFrame 'df' is None. Are you loading the proper .csv file?"
            assert 'genre' in cls.df.columns, "'genre' column not found in DataFrame"
            assert 'platform' in cls.df.columns, "'platform' column not found in DataFrame"

        except Exception as e:
            cls.import_error = str(e)
            raise AssertionError(f"Import error: {cls.import_error}")

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
        self.assertIsNotNone(self.df, "DataFrame 'df' is None. Are you loading the proper .csv file?")
        self.assertIsInstance(self.df, pd.DataFrame, "Variable 'df' is not a pandas DataFrame")
        self.assertFalse(self.df.empty, "DataFrame 'df' should not be empty")

        # Check for required columns
        required_columns = {'platform', 'genre'}
        missing_columns = required_columns - set(self.df.columns)
        self.assertTrue(len(missing_columns) == 0, f"The DataFrame is missing required columns: {missing_columns}")

    def test_filtered_df_creation(self):
        """Test filtered DataFrame creation"""
        self.assertIsNotNone(self.filtered_df, "filtered_df is None")
        self.assertIsInstance(self.filtered_df, pd.DataFrame, "filtered_df is not a pandas DataFrame")

        expected_columns = {'platform', 'genre'}
        actual_columns = set(self.filtered_df.columns)
        self.assertEqual(actual_columns, expected_columns,
                         msg=f"filtered_df should have columns {expected_columns}, but got {actual_columns}")

        actual_platforms = set(self.filtered_df['platform'].unique())
        invalid_platforms = actual_platforms - set(self.filter_list)
        self.assertTrue(len(invalid_platforms) == 0,
                        msg=f"filtered_df contains invalid platforms: {invalid_platforms}. "
                            f"Only {set(self.filter_list)} should be included.")

        self.assertFalse(self.filtered_df.empty, "filtered_df is empty. Check your filtering condition.")

    def test_filter_list(self):
        """Test if filter_list has the correct values"""
        expected_filter_list = {'PS4', 'XOne', 'PC', 'WiiU'}
        actual_filter_list = set(self.filter_list)
        self.assertEqual(actual_filter_list, expected_filter_list,
                         msg=f"filter_list should be {expected_filter_list} but got {actual_filter_list}")

    def test_filtered_df_comparison(self):
        """Compare filtered_df with the expected filtered_df"""
        expected_filtered_df = self.df[self.df['platform'].isin(self.filter_list)][['platform', 'genre']]
        pd.testing.assert_frame_equal(self.filtered_df.reset_index(drop=True),
                                      expected_filtered_df.reset_index(drop=True),
                                      check_dtype=True,
                                      obj='filtered_df does not match the expected filtered DataFrame.')

    def test_genre_counts_comparison(self):
        """Compare genre_counts with the expected genre_counts"""
        expected_genre_counts = self.filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
        pd.testing.assert_frame_equal(self.genre_counts.reset_index(drop=True),
                                      expected_genre_counts.reset_index(drop=True),
                                      check_dtype=True,
                                      obj='genre_counts DataFrame and expected genre_counts DataFrame')

    def test_file_location(self):
        """Test if the file exists in the correct location"""
        file_path = '../dataset.csv'
        if not os.path.exists(file_path):
            self.fail(f"File not found: {file_path}\nMake sure 'dataset.csv' is in the correct location")

        try:
            test_df = pd.read_csv(file_path)
            required_columns = {'platform', 'genre'}
            missing_columns = required_columns - set(test_df.columns)
            self.assertTrue(len(missing_columns) == 0,
                            msg=f"The CSV file is missing required columns: {missing_columns}.\n"
                                f"Expected columns: {required_columns}\nFound columns: {set(test_df.columns)}")
        except Exception as e:
            self.fail(f"File exists but couldn't be read as CSV: {str(e)}")

    def test_genre_counts_order(self):
        """Test if genre_counts is ordered according to platform_order"""
        platform_order = ['PS4', 'XOne', 'PC', 'WiiU']

        # Reindex genre_counts to the specified platform_order
        reindexed_genre_counts = self.genre_counts.reindex(platform_order)

        # Check if the index matches the platform_order
        self.assertListEqual(reindexed_genre_counts.index.tolist(), platform_order,
                             msg=f"genre_counts is not in the correct order. Expected: {platform_order}, Got: {reindexed_genre_counts.index.tolist()}")

    def test_genre_counts_not_empty(self):
        """Test if genre_counts is not empty after reindexing"""
        platform_order = ['PS4', 'XOne', 'PC', 'WiiU']
        reindexed_genre_counts = self.genre_counts.reindex(platform_order)

        self.assertFalse(reindexed_genre_counts.empty, "genre_counts should not be empty after reindexing.")

    @patch('matplotlib.pyplot.show')
    def test_plotting(self, mock_show):
        """Test if plotting functions are called correctly"""
        platform_order = ['PS4', 'XOne', 'PC', 'WiiU']
        genre_counts_reindexed = self.genre_counts.reindex(platform_order)

        # Call the plotting code
        genre_counts_reindexed.plot(kind='bar', figsize=(10, 6))
        plt.xlabel('platform')
        plt.ylabel('count')
        plt.xticks(rotation=0)
        plt.legend(title='genre')
        plt.tight_layout()
        plt.show()  # This should be mocked

        # Verify that the relevant plotting functions were called
        mock_show.assert_called_once()
        self.assertEqual(len(plt.get_fignums()), 1, "A single figure should be created.")

        # Check the labels
        self.assertEqual(plt.gca().get_xlabel(), 'platform')
        self.assertEqual(plt.gca().get_ylabel(), 'count')


if __name__ == "__main__":
    unittest.main()
