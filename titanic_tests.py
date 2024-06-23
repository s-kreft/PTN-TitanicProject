import unittest
from service.Service import Service
import numpy as np
import pandas as pd

class TitanicTests(unittest.TestCase):
    def __init__(self, input):
        self.service = Service()
    
    def test_search_titanic_data_return_only_male(self):
        df = self.service.search_male_titanic_data
        contains_test = df['Płeć'].str.contains('male')
        self.assertTrue(contains_test)

if __name__ == '__main__':
    unittest.main()