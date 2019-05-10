import matplotlib.pyplot as plt
# import tkinter as tk


class Matplotbasics:
    @staticmethod
    def twoline_sameplot():

        # plotting the line 1 points
        x1 = [20, 40, 60]
        y1 = [30, 40, 60]
        plt.plot(x1, y1, label="first line")

        # plotting the line 2 points
        x2 = [10, 40, 50]
        y2 = [30, 20, 40]

        plt.plot(x2, y2, label="second line")

        plt.xlabel('This is x - axis')
        plt.ylabel('This is y - axis')
        plt.title('Two or more lines on same plot with suitable legends')
        plt.legend()
        plt.show()

    @staticmethod
    def twoline_sameplot_width_color():

        x1 = [10, 20, 30]
        y1 = [20, 40, 10]

        x2 = [10, 20, 30]
        y2 = [40, 10, 30]

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.plot(x1, y1, color='orange', linewidth=2, label='first_line-width-2')

        plt.title('Two or more lines on same plot different widths and colors with suitable legends ')
        plt.plot(x2, y2, color='purple', linewidth=5, label='second_line-width-5')

        plt.legend()
        plt.show()

    @staticmethod
    def twoline_sameplot_diff_style():
        x1 = [10, 20, 30]
        y1 = [20, 40, 10]

        x2 = [10, 20, 30]
        y2 = [40, 10, 30]

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.title('Plot with two or more lines with different styles')

        plt.plot(x1, y1, color='orange', linewidth=3, label='first_line-dotted', linestyle='dotted')
        plt.plot(x2, y2, color='purple', linewidth=5, label='second_line-dashed', linestyle='dashed')

        plt.legend()
        plt.show()


# Matplotbasics.twoline_sameplot()
# Matplotbasics.twoline_sameplot_width_color()
# Matplotbasics.twoline_sameplot_diff_style()



