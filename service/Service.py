import numpy as np
import pandas as pd
from model.Passenger import Passenger

class Service:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Service, cls).__new__(cls)
        return cls.instance

    def TitanicData(self):
        pd.set_option('display.max_rows', 900)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        titanic_data = pd.read_csv("data/Titanic-Dataset.csv", index_col=0)
        # titanic_data.head()
        self.titanic_dataframe = pd.DataFrame(titanic_data)
        print(self.titanic_dataframe)


        #print(self.titanic_dataframe.loc['Fare' > 10])

    def LocateTitanicData(self):
        self.titanic_dataframe.loc['Sarah']



