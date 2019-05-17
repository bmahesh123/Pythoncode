import matplotlib.pyplot as plt
import tkinter as tk


class MatplotlibBasics:
    @staticmethod
    def drawline():
        x = range(1, 50)

        y = [value * 2 for value in x]
        print("Value of X:")
        print(*range(1, 50))
        print("Values of y (twice of x):")
        print(y)

        plt.plot(x, y)
        # Set the x axis label of the current axis.
        plt.xlabel('This is X - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('This is Y - axis')
        # Set a title for graph
        plt.title('Draw a line using Mat-plot-lib and Tkinter')
        plt.show()


MatplotlibBasics.drawline()