import numpy as np
import pandas as pd
import pandas.core.frame
import matplotlib.pyplot as plt


class Service:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Service, cls).__new__(cls)
        return cls.instance

    def __init__(self, titanic_dataframe = None):
        self.titanic_dataframe = titanic_dataframe
        #self.titanic_dataframe = pandas.core.frame.DataFrame


    def titanic_data(self):
        pd.set_option('display.max_rows', 900)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        titanic_data = pd.read_csv("data/Titanic-Dataset.csv")
        # titanic_data.head()
        titanic_columns = ['Id', 'Przeżył/a', 'Klasa podróży', 'Imię', 'Płeć',
                   'Wiek', 'Rodzeństwo/Małżonek', 'Rodzice/Dzieci', 'Numer Biletu', 'Koszt', 'Numer Kabiny',
                   'Miejsce Zaokrętowania']
        self.titanic_dataframe = pd.DataFrame(titanic_data)
        self.titanic_dataframe.columns = titanic_columns
        self.titanic_dataframe.set_index('Id', inplace=True)
        self.titanic_dataframe = self.titanic_dataframe.drop('Imię', axis=1)


    def show_titanic_data(self):
        return print(self.titanic_dataframe.head())


    def search_titanic_data(self, user_input):
       # return print(self.titanic_dataframe.loc[self.titanic_dataframe['Wiek'] < int(userInput)])

       return print(self.titanic_dataframe.loc[self.titanic_dataframe['Płeć'] == 'male'])

    def search_titanic_age(self, search_input):
        user_input = input("Wybierz operator <, > lub =\n")
        if user_input == '<':
            return print(self.titanic_dataframe.loc[self.titanic_dataframe['Wiek'] < int(search_input)])
        elif user_input == '>':
            return print(self.titanic_dataframe.loc[self.titanic_dataframe['Wiek'] > int(search_input)])
        elif user_input == '=':
            return print(self.titanic_dataframe.loc[self.titanic_dataframe['Wiek'] == int(search_input)])
        else:
            return print("Niedozwolona operacja")

    def titanic_age_pie_chart(self):
        plt.hist(self.titanic_dataframe.loc[self.titanic_dataframe['Wiek']])
        plt.show()
    def titanic_age_plot(self):
        plt.figure(figsize=(8, 6))
        self.titanic_dataframe['Wiek'].value_counts().plot(kind='bar', color='skyblue')
        return plt.show()

