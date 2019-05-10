# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics7:
    @staticmethod
    def selection_row_check_condition():

        dataframe_dict = {'Name': ['Mahesh', 'vinay', 'Kailash', 'Dhiraj', 'Viren', 'Mayur'],
                          'Age': [25, 30, 32, 35, 45, 60],
                          'Pass_out_year': [2015, 2014, 2015, 2015, 2012, 2014],
                          'Qualification': ['MS', 'BE', 'BSC.IT', 'MSC.IT', 'BTECH', 'BE']}

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        df = pd.DataFrame(dataframe_dict, index=labels)
        print(df)
        print(" ")
        print("Rows where age greater 25:")
        print(df[(df['Age'] > 25)])


PandasBasics7.selection_row_check_condition()

