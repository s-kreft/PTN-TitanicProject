import unittest
from service.Service import Service
import numpy as np
import pandas as pd

class TitanicTests(unittest.TestCase):
    
    def test_search_titanic_data_returns_only_male(self):
        self.service = Service()
        user_input = 'm'
        df = self.service.search_gender_titanic_data(user_input)
        contains_male = all(self.service.contemporary_data_frame['Płeć'].str.fullmatch('male'))
        self.assertTrue(contains_male)

    # def test_quick(self):
    #     number_one = 2
    #     number_two = 2
    #     self.assertEqual(number_one, number_two)

if __name__ == '__main__':
    unittest.main()