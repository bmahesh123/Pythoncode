import seaborn as sb
from matplotlib import pyplot as plt


class Seaborn_pointplot:
    @staticmethod
    def draw_point_plot():
        dataframe = sb.load_dataset('titanic')
        sb.pointplot(x="sex", y="survived", hue="class", data=dataframe)
        plt.title('Point plot for sex against survived')
        plt.show()


Seaborn_pointplot.draw_point_plot()

