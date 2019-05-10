# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics3:
    @staticmethod
    def power_array_element():

        # creating numpy array
        data = np.arange(7)
        print("Array element:")
        print(data)
        print("First array elements raised to powers from second array| element-wise:")
        print(np.power(data, 3))
        print(np.power(data, 4))


PandasBasics3.power_array_element()


