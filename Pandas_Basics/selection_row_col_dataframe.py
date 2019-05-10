# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics6:
    @staticmethod
    def selection_col_data_frame():

        dataframe_dict = {'Name': ['Mahesh', 'vinay', 'Kailash', 'Dhiraj', 'Viren', 'Mayur'],
                          'Age': [25, 24, np.nan, 29, 25, 26],
                          'Pass_out_year':[2015, 2014,2015,2015,2012,2014],
                          'Qualification': ['MS', 'BE', 'BSC.IT', 'MSC.IT', 'BTECH', 'BE']}

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        datafram = pd.DataFrame(dataframe_dict, index=labels)
        print(datafram)
        print(" ")
        print("Select specific columns and rows: ")
        df1 = (datafram.iloc[[0, 1, 3, 5], [0, 2, 3]])
        print(df1)


PandasBasics6.selection_col_data_frame()
