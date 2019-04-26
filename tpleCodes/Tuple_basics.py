from copy import deepcopy


class Tuple:
    @staticmethod
    def createTuple(self):
        tup = ('Mango', 'Apple', 'boy', 'girl', 20, 40, 50,80)
        print(tup)

    def diff_dat_ty(self):
        tup = ('Mango', 'Apple', 'boy', 'girl', 2.0, 4.02, 8.215)
        print(tup)

    def unpack_tup(self):
        tup = (20 , 40 , 50 , 80)
        print(tup)
        t1, t2, t3, t4 = tup
        print(t1 + t2 + t3 + t4 )
        t1, t2, t3, t4 =tup
        print(t1, t2, t3, t4)


    # Copy a tuple using deepcopy
    def clone_tup(self):

        tup = ('Hi Mahesh', 'you', 'can', 'do', 'it',  [], 'True')
        print(tup)
        # copy of a tuple using deepcopy() func
        tupl_clon = deepcopy(tup)
        tupl_clon[5].append(100)
        print(tupl_clon)

    def repet_tuple(self):
        tupl = (2, 4, 5, 6, 2, 3, 4, 4, 7, 8, 9, 4, 4, 4, 10, 4, 4, 20)
        print(tupl)
        count = tupl.count(4)
        print(count)

    def exist_tuple(self):
        tupl = (2, 4, 5, 6, 2, 3, 4, 4, 7, 8, 9, 4, 4, 4, 10, 4, 4, 20)
        print(tupl)
        print(2 in tupl)
        print("Ma" in tupl)
        print(-4 in tupl)
        print('$' in tupl)
        print(20 in tupl)

    def convert_lt_tup(lis):
        return tuple(lis)
    lis = [2, 4, 5, 6, 2, 7, 8, 9]
    print(lis)
    print(convert_lt_tup(lis))

    def rem_tupl(self):
        tup = (2, 4, 5, 6, 2, 7, 8, 9)
        print(tup)
        ls = list(tup)
        ls.remove(2)
        print(ls)

    def slic_tupl(self):
        tupe = tuple('Hello World')
        print(tupe)
        slice = tupe[0:8]
        print(slice)

    def revers_tupl(self):
        tupe = tuple('Hello Mahesh')
        print("Tuple before reverse:", tupe)
        rev_tup = tupe[::-1]
        print("Tuple after reverse:", rev_tup)


#
# Tuple.createTuple(" ")
# Tuple.diff_dat_ty(" ")
# Tuple.unpack_tup(" ")
# Tuple.clone_tup(" ")
# Tuple.repet_tuple(" ")
# Tuple.exist_tuple(" ")
# # Tuple.convert(list)   #need to uncomment print statement from func
# Tuple.rem_tupl(" ")
# Tuple.slic_tupl(" ")
# Tuple.revers_tupl(" ")
