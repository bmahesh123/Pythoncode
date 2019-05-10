import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np


class MatplotlibBasics:
    @staticmethod
    def plot_line():
        x = np.array(input('Enter value for x axis:').split(","), dtype = int)
        y = np.array(input('Enter value for y axis:').split(","), dtype = int)

        plt.plot(x, y)
        plt.xlabel('This is X - axis')
        plt.ylabel('This is Y - axis')
        plt.title('User access graph')
        plt.show()


MatplotlibBasics.plot_line()