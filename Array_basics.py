from array import *


class Array:

    @staticmethod
    def cretarr(self):
        arr = array('i', [1,2,3,4,5])
        for i in arr:
            print(i)

        print("Access first two item from array")

        print(arr[0])
        print(arr[1])


    def revarr(self):
        arr = array('i', [1, 2, 3, 4, 5])
        print("Array before reverse:", arr)
        print("Array after reverse:", arr[::-1])
        print("Array after reverse:", arr.reverse())
        for i in arr:
            print(i)


    def occ_arr(self):
        arr = array('i', [1, 2, 3, 3, 8, 5, 6, 8, 5, 4, 5, 2, 8, 2, 9, 8, 8, 8, 2])
        arr = arr.count(8)
        print(arr)


    def removearr(self):
        arr = array('i', [1, 2, 3, 4, 5, 6, 8, 3])
        arr10 = list(arr)
        print("Before removing element from array:", arr10)
        arr10.remove(3)
        print("After removing element from array:", arr10)


# Array.cretarr(" ")
# Array.revarr(" ")
# Array.occ_arr(" ")
# Array.removearr(" ")

