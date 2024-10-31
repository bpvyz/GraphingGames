import unittest

class TestPandasInstallation(unittest.TestCase):
    def test_pandas_import(self):
        try:
            import pandas as pd
            self.assertTrue(True, "Pandas is installed.")
        except ImportError:
            self.fail("Pandas is not installed.")

if __name__ == '__main__':
    unittest.main()
