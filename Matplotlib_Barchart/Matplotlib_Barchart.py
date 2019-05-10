import matplotlib.pyplot as plt

class MatBarchart:
    @staticmethod
    def displaybarchart():

        pl = ['Python', 'Java', 'HTML', 'SQL', 'Spring', '.Net']
        popularity = [22.2, 18.6, 15.8, 14.2, 20.2, 12.7]
        pl_pos = [i for i, _ in enumerate(pl)]
        plt.bar(pl_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

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


MatBarchart.displaybarchart()
