import seaborn as sb
from matplotlib import pyplot as plt


class Seaborn_Bar_plot:
    @staticmethod
    def draw_bar_plot():
        dataframe = sb.load_dataset('titanic')
        sb.barplot(x="sex", y="survived", hue="class", data=dataframe)
        plt.title('Bar plot for Sex against Survived ')
        plt.show()


Seaborn_Bar_plot.draw_bar_plot()
