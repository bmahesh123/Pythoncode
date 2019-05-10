# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics:
    @staticmethod
    def one_dim_array_panda():

        # creating numpy array
        data = np.array([1, 2, 3, 4, 5])
        data2 = np.array(['H', 'E', 'L','L', 'O'])
        # creating series
        ser = pd.Series(data)
        ser2= pd.Series(data2)
        print(ser)
        print(ser2)


PandasBasics.one_dim_array_panda()


