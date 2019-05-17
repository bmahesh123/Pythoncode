import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np


class MatplotlibBasics:
    @staticmethod
    def plot_line_txt():
        with open("mat_test.txt") as file:
            data = file.read()
        data = data.split('\n')
        x = [row.split(' ')[0] for row in data]
        y = [row.split(' ')[1] for row in data]
        x = np.array(x, dtype=int)
        y = np.array(y, dtype=int)
        print("Value of x:", x)
        print("Value of y:", y)
        plt.plot(x, y)
        # Set the x axis label of the current axis.
        plt.xlabel('This is x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('This is y - axis')
        # Set a title
        plt.title('User access graph!')
        # Display a figure.
        plt.show()

MatplotlibBasics.plot_line_txt()