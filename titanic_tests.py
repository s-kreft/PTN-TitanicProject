import unittest
from unittest.mock import patch
from service.Service import Service
import numpy as np
import pandas as pd

def get_user_input():
    return input("<")

class TitanicTests(unittest.TestCase):
    
    def test_search_titanic_data_returns_only_male(self):
        self.service = Service()
        user_input = 'm'
        self.service.search_gender_titanic_data(user_input)
        contains_male = all(self.service.contemporary_data_frame['Płeć'].str.fullmatch('male'))
        self.assertTrue(contains_male)
    
    @patch('builtins.input', return_value='<')
    def test_search_age_is_lesser_than(self, mocked_input):
        self.service = Service()
        user_input = '20'
        self.service.search_titanic_age(user_input)
        age_test = all(self.service.contemporary_data_frame['Wiek'] < 20)
        self.assertTrue(age_test)

    def test_search_titanic_is_alive(self):
        self.service = Service()
        user_input = '1'
        self.service.search_titanic_alive(user_input)
        alive_test = all(self.service.contemporary_data_frame['Przeżył/a'] == 1)
        self.assertTrue(alive_test)



    # def test_quick(self):
    #     number_one = 2
    #     number_two = 2
    #     self.assertEqual(number_one, number_two)

if __name__ == '__main__':
    unittest.main()