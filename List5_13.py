import operator


class List5:
    @staticmethod
    def sort_list_tuple():
    # def sort_list_tuple(self):

        list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        temp = sorted(list, key=operator.itemgetter(1))
        print(temp)


List5.sort_list_tuple()
# List5.sort_list_tuple("")

# obj = List5()
# obj.sort_list_tuple()


