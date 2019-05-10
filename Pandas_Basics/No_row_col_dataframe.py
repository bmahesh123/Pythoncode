# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics8:
    @staticmethod
    def no_row_col_df():

        df_dict = {'Name': ['Mahesh', 'vinay', 'Kailash', 'Dhiraj', 'Viren', 'Mayur'],
                            'Age': [25, 30, 32, 35, 45, 60],
                            'Pass_out_year': [2015, 2014, 2015, 2015, 2012, 2014],
                            'Qualification': ['MS', 'BE', 'BSC.IT', 'MSC.IT', 'BTECH', 'BE']}

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        df = pd.DataFrame(df_dict, index=labels)
        print(" ")
        print(df)
        print(" ")
        total_no_rows = len(df.axes[0])
        total_no_cols = len(df.axes[1])
        print("No of rows in DF:" + str(total_no_rows))
        print("No of cols in DF:" + str(total_no_cols))


PandasBasics8.no_row_col_df()

