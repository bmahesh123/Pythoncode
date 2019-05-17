import seaborn as sb
from matplotlib import pyplot as plt


class Seaborn_pointplot:
    @staticmethod
    def draw_point_plot():
        dataframe = sb.load_dataset('tips')
        sb.scatterplot(x="total_bill", y="day", data=dataframe)
        plt.title('Scatter plot of Day against Total bill')
        plt.show()


Seaborn_pointplot.draw_point_plot()
