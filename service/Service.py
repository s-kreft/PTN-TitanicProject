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
        self.contemporary_data_frame = None
        self.titanic_data()

    def titanic_data(self):
        pd.set_option('display.max_rows', 900)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        titanic_data = pd.read_csv("data/Titanic-Dataset.csv")

        titanic_columns = ['Id', 'Przeżył/a', 'Klasa podróży', 'Imię', 'Płeć',
                   'Wiek', 'Rodzeństwo/Małżonek', 'Rodzice/Dzieci', 'Numer Biletu', 'Koszt', 'Numer Kabiny',
                   'Miejsce Zaokrętowania']
        self.titanic_dataframe = pd.DataFrame(titanic_data)
        self.titanic_dataframe.columns = titanic_columns
        self.titanic_dataframe.set_index('Id', inplace=True)
        self.titanic_dataframe = self.titanic_dataframe.drop('Imię', axis=1)
        self.contemporary_data_frame = self.titanic_dataframe

    def show_titanic_data(self):
        return print(self.contemporary_data_frame)

    def search_gender_titanic_data(self, gender_input):
       if gender_input == 'k':
           self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Płeć'] == 'female']
           return print(self.contemporary_data_frame)
       elif gender_input == 'm':
            self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Płeć'] == 'male']
            return print(self.contemporary_data_frame)
       else:
            return print("Niedozwolona operacja")

    def search_titanic_age(self, search_input):
        user_input = input("Wybierz operator <, > lub =\n")
        if user_input == '<':
            self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Wiek'] < int(search_input)]
            return print(self.contemporary_data_frame)
        elif user_input == '>':
            self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Wiek'] > int(search_input)]
            return print(self.contemporary_data_frame)
        elif user_input == '=':
            self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Wiek'] == int(search_input)]
            return print(self.contemporary_data_frame)
        else:
            return print("Niedozwolona operacja")
    
    def search_titanic_alive(self, alive_input):
        if alive_input == '1':
           self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Przeżył/a'] == 1]
           return print(self.contemporary_data_frame)
        elif alive_input == '0':
            self.contemporary_data_frame = self.contemporary_data_frame.loc[self.contemporary_data_frame['Przeżył/a'] == 0]
            return print(self.contemporary_data_frame)
        else:
            return print("Niedozwolona operacja")

    def titanic_is_alive_pie_chart(self):
        counts = self.contemporary_data_frame['Przeżył/a'].value_counts()
        labels = ['Przeżyło', 'Nie Przeżyło']
        sizes = [counts[1], counts[0]]
        colors = ['green', 'grey']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True, explode=[0.12, 0])
        plt.axis('equal')
        plt.title("Procent osób, które przeżyły")
        return plt.show()

    def titanic_age_plot(self):
        age_counts = self.contemporary_data_frame['Wiek'].value_counts().sort_index()
        plt.figure(figsize=(8, 6))
        plt.bar(age_counts.index, age_counts.values, color='skyblue')
        plt.xlabel("Wiek w latach")
        plt.ylabel("Liczba osób")
        plt.title("Liczba osób w poszczególnych grupach wiekowych")
        return plt.show()

    def data_frame_reset(self):
        self.contemporary_data_frame = self.titanic_dataframe
        return print("Zresetowano dane wyszukiwania")