class List9:
    # def compare(list1,list2):
    #     op = False
    #     for x in list1:
    #         for y in list2:
    #             if x == y:
    #                 op = True
    #                 return op
    #
    # print(compare([12, 30, 44, 100, 20], [11, 16, 79, 20, 88, 99]))

    @staticmethod
    def compare(self):
        list3 =[12, 30, 44, 100]
        list4 =[11, 16, 79,  88, 99, 200]
        set1 = set(list3)
        set2 = set(list4)
        val = len(set1.intersection(set2))
        print(val)
        if val > 0:
            print("True")
        else:
            print("False")


List9.compare(" ")




