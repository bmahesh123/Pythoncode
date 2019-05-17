import seaborn as sb
from matplotlib import pyplot as plt


class Seaborn_pointplot:
    @staticmethod
    def draw_point_plot():
        dataframe = sb.load_dataset('iris')
        sb.violinplot(x="total_bill", y="day", data=dataframe)
        plt.title('violin plot of sex against survived')
        plt.show()


Seaborn_pointplot.draw_point_plot()