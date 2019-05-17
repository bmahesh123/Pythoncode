import matplotlib.pyplot as plt
import pandas as pd


class Csvfile:
    @staticmethod
    def draw_line_csv():
        df = pd.read_csv('findata.csv')
        print(df)
        df.plot()
        plt.show()


Csvfile.draw_line_csv()

