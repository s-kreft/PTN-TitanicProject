import unittest
from unittest.mock import patch
from service.Service import Service
import numpy as np
import pandas as pd
class TitanicTests(unittest.TestCase):
    
    def test_search_titanic_data_returns_only_male(self):
        self.service = Service()
        user_input = 'm'
        self.service.search_gender_titanic_data(user_input)
        contains_male = all(self.service.contemporary_data_frame['Płeć'].str.fullmatch('male'))
        self.assertTrue(contains_male)

    def test_search_titanic_data_returns_only_female(self):
        self.service = Service()
        user_input = 'k'
        self.service.search_gender_titanic_data(user_input)
        contains_female = all(self.service.contemporary_data_frame['Płeć'].str.fullmatch('female'))
        self.assertTrue(contains_female)

    @patch('builtins.input', return_value='<')
    def test_search_age_is_lesser_than_20(self, mock_input):
        self.service = Service()
        user_input = '20'
        self.service.search_titanic_age(user_input)
        age_test = all(self.service.contemporary_data_frame['Wiek'] < 20)
        self.assertTrue(age_test)

    @patch('builtins.input', return_value='>')
    def test_search_age_is_greater_than_20(self, mock_input):
        self.service = Service()
        user_input = '20'
        self.service.search_titanic_age(user_input)
        age_test = all(self.service.contemporary_data_frame['Wiek'] > 20)
        self.assertTrue(age_test)
    
    @patch('builtins.input', return_value='=')
    def test_search_age_equals_20(self, mock_input):
        self.service = Service()
        user_input = '20'
        self.service.search_titanic_age(user_input)
        age_test = all(self.service.contemporary_data_frame['Wiek'] == 20)
        self.assertTrue(age_test)

    def test_search_titanic_is_alive(self):
        self.service = Service()
        user_input = '1'
        self.service.search_titanic_alive(user_input)
        alive_test = all(self.service.contemporary_data_frame['Przeżył/a'] == 1)
        self.assertTrue(alive_test)
    
    def test_search_titanic_is_not_alive(self):
        self.service = Service()
        user_input = '0'
        self.service.search_titanic_alive(user_input)
        not_alive_test = all(self.service.contemporary_data_frame['Przeżył/a'] == 0)
        self.assertTrue(not_alive_test)

if __name__ == '__main__':
    unittest.main()