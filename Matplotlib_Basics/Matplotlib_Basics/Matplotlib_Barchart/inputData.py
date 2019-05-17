
class MatBarchart_Data(object):
    def __init__(self):
        self.x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        self.popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    def input_data_matplot_lib(self):

        lst_x = self.x
        lst_pop = self.popularity

        return lst_x, lst_pop
