import matplotlib.pyplot as plt
from Matplotlib_Barchart.inputData import *


class MatBarchart(MatBarchart_Data):

    """ Using OOPS concept:  Inheritance"""

    def __init__(self):
        MatBarchart_Data.__init__(self)

    def displaybarchart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)
        pl_pos = [i for i, _ in enumerate(pl)]
        plt.bar(pl_pos, pop, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide")
        plt.xticks(pl_pos, pl)

        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()


    def display_horizontal_barchart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)
        pl_pos = [i for i, _ in enumerate(pl)]
        plt.barh(pl_pos, pop, color='red', edgecolor='black')

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide")
        plt.yticks(pl_pos, pl)

       # Turn on the grid

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()


    def uniform_color_barchart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)

        pl_pos = [i for i, _ in enumerate(pl)]
        # Using Uniform color
        plt.bar(pl_pos, pop, color=(0.2, 0.4, 0.6, 0.6), edgecolor='black')

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide ")
        plt.xticks(pl_pos, pl)

       # Turn on the grid

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()



    def diff_color_barchart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)

        pl_pos = [i for i, _ in enumerate(pl)]
        # Using Uniform color
        plt.bar(pl_pos, pop, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide ")
        plt.xticks(pl_pos, pl)

       # Turn on the grid

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='blue')
        plt.show()


    def Barchart_popularity(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)

        pl_pos = [i for i, _ in enumerate(pl)]
        fig, ax = plt.subplots()
        graph = ax.bar(pl_pos, pop, color='R')

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide")
        plt.xticks(pl_pos, pl)

        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%f' % float(height),
                        ha='center', va='bottom')

        autolabel(graph)
        plt.show()


    def edgecolor_barchart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)
        pl_pos = [i for i, _ in enumerate(pl)]

        """ Make blue border to each bar using edgecolor"""
        plt.bar(pl_pos, pop, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

        plt.xlabel("Programing Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language\n" + "Worldwide")
        plt.xticks(pl_pos, pl)

        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()


obj = MatBarchart()
# obj.displaybarchart()
# obj.display_horizontal_barchart()
# obj.uniform_color_barchart()
# obj.diff_color_barchart()
# obj.Barchart_popularity()
obj.edgecolor_barchart()
