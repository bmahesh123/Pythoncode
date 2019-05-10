# importing Pandas & numpy
import pandas as pd
import numpy as np


class PandasBasics2:
    @staticmethod
    def add_sub_mul_div_panda():

        # creating numpy array
        data = np.array([1, 12, 43, 84, 15])
        data2 = np.array([1, 3, 5, 7, 9])
        # creating series
        ser = pd.Series(data)
        ser2= pd.Series(data2)
        print("Addition two panda series:")
        adds = ser + ser2
        print(adds)

        print("Subtraction two panda series:")
        subs = ser - ser2
        print(subs)

        print("Multiplication two panda series:")
        muls = ser * ser2
        print(muls)

        print("Division two panda series:")
        divs = ser / ser2
        print(divs)


PandasBasics2.add_sub_mul_div_panda()


