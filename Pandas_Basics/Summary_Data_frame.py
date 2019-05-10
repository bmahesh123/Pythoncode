# importing Pandas & numpy
import pandas as pd
import numpy as np

class PandasBasics4:
    @staticmethod
    def creation_data_frame_dict_index():

        dataframe_dict = {'Name': ['Mahesh', 'vinay', 'Kailash', 'Dhiraj'],
                          'Age': [25, 24, 28, 29],
                          'Pass_out_year':[2015, 2014,2015,2015],
                          'Qualification': ['BE', 'BE', 'BSC.IT', 'MSC.IT']}

        labels = ['A', 'B', 'C', 'D']
        datafram = pd.DataFrame(dataframe_dict, index=labels)
        print(datafram)
        print(" ")
        print("Summary of the basic information about this DataFrame and its data:")
        print(datafram.info())


PandasBasics4.creation_data_frame_dict_index()