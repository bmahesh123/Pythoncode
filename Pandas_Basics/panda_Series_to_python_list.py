# importing Pandas & numpy
import pandas as pd


class PandasBasics1:
    @staticmethod
    def panda_series_py_list():

        # creating series
        ser = pd.Series([1, 2, 3, 4, 5])
        print("Pandas Series and type")
        print(ser)
        print(type(ser))
        print(" ")
        print("Convert Pandas Series to Python list:")
        print(ser.tolist())
        print(type(ser.tolist()))


PandasBasics1.panda_series_py_list()


