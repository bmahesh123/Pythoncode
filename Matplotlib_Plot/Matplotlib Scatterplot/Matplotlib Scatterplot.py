import matplotlib.pyplot as plt
from pylab import randn
import numpy as np
import math
import random
import pandas as pd

class Scatter_graph:
    @staticmethod
    def scatter_random_distribution():
        # create random data
        No1 = randn(200)
        No2 = randn(200)
        plt.scatter(No1, No2, color='b')
        plt.xlabel("X - Axis")
        plt.ylabel("Y - Axis")
        plt.show()

    def scatter_random_distribution_empty_circles():
        # create random data
        No1 = np.random.randn(100)
        No2 = np.random.randn(100)
        plt.scatter(No1, No2, s=70, facecolors='none', edgecolors='g')
        plt.xlabel("X - Axis")
        plt.ylabel("Y - Axis")
        plt.show()

    def scatter_random_distribution_generate_balls():

        # create random data
        no_of_balls = 25
        No1 = [random.triangular() for i in range(no_of_balls)]
        No2 = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
        colors = [random.randint(1, 4) for i in range(no_of_balls)]
        areas = [math.pi * random.randint(5, 15) ** 2 for i in range(no_of_balls)]

        # draw the plot
        plt.figure()
        plt.scatter(No1, No2, s=areas, c=colors, alpha=0.85)
        plt.axis([0.0, 1.0, 0.0, 1.0])
        plt.xlabel("X - Axis")
        plt.ylabel("Y - Axis")
        plt.show()

    def scatter_plot_compare():
        sci_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
        math_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
        marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        plt.scatter(marks_range, sci_marks, label='Math marks', color='b')
        plt.scatter(marks_range, math_marks, label='Science marks', color='g')

        plt.title('Scatter Plot comparing two subject marks')
        plt.xlabel('Marks - Range')
        plt.ylabel('Marks - Scored')
        plt.legend()
        plt.show()

    def scatter_plot_three_grp_compare():

        weight1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56]
        height1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9]

        weight2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6]
        height2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1]

        weight3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7]
        height3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3]

        grp_weight = np.concatenate((weight1, weight2, weight3))
        grp_height = np.concatenate((height1, height2, height3))

        colors = [random.randint(1, 4) for i in range(len(grp_weight))]

        plt.scatter(grp_weight, grp_height, marker='+', c=colors)
        plt.xlabel('Group wise Weight', fontsize=12)
        plt.ylabel('Group wise Height', fontsize=12)
        plt.title('Group wise Weight vs Height scatter plot', fontsize=16)
        plt.show()


# Scatter_graph.scatter_random_distribution()
# Scatter_graph.scatter_random_distribution_empty_circles()
Scatter_graph.scatter_random_distribution_generate_balls()
# Scatter_graph.scatter_plot_compare()
# Scatter_graph.scatter_plot_three_grp_compare()



