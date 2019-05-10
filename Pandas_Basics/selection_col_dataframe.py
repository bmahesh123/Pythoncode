# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics5:
    @staticmethod
    def selection_col_data_frame():

        dataframe_dict = {'Name': ['Mahesh', 'vinay', 'Kailash', 'Dhiraj'],
                          'Age': [25, 24, np.nan, 29],
                          'Pass_out_year':[2015, 2014,2015,2015],
                          'Qualification': ['BE', 'BE', 'BSC.IT', 'MSC.IT']}

        labels = ['A', 'B', 'C', 'D']
        datafram = pd.DataFrame(dataframe_dict, index=labels)
        print(datafram)
        print(" ")
        print("Select specific columns from data frame:")
        print(datafram[['Name', 'Qualification']])
        print(" ")
        print(datafram[['Pass_out_year', 'Age']])


PandasBasics5.selection_col_data_frame()
