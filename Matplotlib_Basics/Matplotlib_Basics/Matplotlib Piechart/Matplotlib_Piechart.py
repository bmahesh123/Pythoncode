import matplotlib.pyplot as plt
from Matplotlib_Barchart.inputData import *
import pandas as pd


class Piechart(MatBarchart_Data):

    """ Using OOPS concept:  Inheritance"""

    def __init__(self):
        MatBarchart_Data.__init__(self)

    def displaypiechart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)

        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        # explode 1st slice
        explode = (0.1, 0, 0, 0, 0, 0)
        # Plot
        plt.pie(pop, explode=explode, labels=pl, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=100)

        plt.axis('equal')
        plt.show()

    def add_title_piechart(self):

        # Inherit method of parent class name input_data_matplot_lib()

        data_obj = MatBarchart_Data()
        data = data_obj.input_data_matplot_lib()

        tuple_to_list = list(data)
        pl = tuple_to_list[0]
        pop = tuple_to_list[1]
        print(pl)
        print(pop)

        colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
        # explode 1st slice
        explode = (0.1, 0, 0, 0, 0, 0)
        # Plot
        plt.pie(pop, explode=explode, labels=pl, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=100)

        plt.title("PopularitY of Programming Language\n" + "Worldwide",
                  bbox={'facecolor': '0.8', 'pad': 5})

        plt.show()


    def piechart_using_csv(self):

        dataframe = pd.read_csv('medal.csv')
        country_data = dataframe["country"]
        medal_data = dataframe["gold_medal"]
        colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0, 0)
        plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title("Gold medal achievements of five most successful\n" + "countries in 2016 Summer Olympics")
        plt.show()

obje = Piechart()
# obje.displaypiechart()
# obje.add_title_piechart()
obje.piechart_using_csv()