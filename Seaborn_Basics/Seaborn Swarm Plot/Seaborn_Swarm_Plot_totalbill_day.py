import seaborn as sb
from matplotlib import pyplot as plt


class Seaborn_pointplot:
    @staticmethod
    def draw_point_plot():
        dataframe = sb.load_dataset('tips')
        sb.swarmplot(x="total_bill", y="day", data=dataframe)
        plt.title('Seaborn Swarm Plot Total Bill vs Day')
        plt.show()


Seaborn_pointplot.draw_point_plot()