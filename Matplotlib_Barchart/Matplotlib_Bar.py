import matplotlib.pyplot as plt
from Matplotlib_Barchart.inputData import *


class MatBarchart(object, MatBarchart_Data):

    def displaybarchart(self):

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
        plt.title("Popularity of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
        plt.xticks(pl_pos, pl)

        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()


matbarchart_Data = MatBarchart_Data()
MatBarchart.displaybarchart()
