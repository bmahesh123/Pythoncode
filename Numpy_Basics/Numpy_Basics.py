import numpy as np


class NumpyBasics:
    @staticmethod
    def list_one_dim_array():

        before_con= [12.23, 13.32, 100, 36.32]
        print("Before convert:", before_con)

        after_con = np.array([12.23, 13.32, 100, 36.32])
        print("After convert One Dimensional data:", after_con)

    @staticmethod
    def matrices_reshape():

        array1 = np.arange(2, 11)
        # print(array1)
        array2 = array1.reshape(3, 3)
        print(array2)

    @staticmethod
    def null_vector():
        array1 = np.zeros(10)
        print(array1)
        array1[6] = 11
        print("After Update sixth value to 11:")
        print(array1)

    @staticmethod
    def reverse_numpy():
        array1 = np.arange(12, 38)
        print("Original array:")
        print(array1)
        print("Reverse array:")
        array2 = array1[::-1]
        print(array2)

    @staticmethod
    def two_d_border():
        array1 = np.ones(25)
        print("Original array:")
        array2 = array1.reshape(5, 5)
        print(array2)
        array2[1:-1, 1:-1] = 0
        print(array2)

    @staticmethod
    def add_zero_border():
        # array1 = np.zeros(25)
        # print("Original array:")
        # array2 = array1.reshape(5, 5)
        # print(array2)
        # print("After add 1 on the border:")
        # array2[1:-1, 1:-1] = 1
        # print(array2)

        array1 = np.ones(9)
        print("Original array:")
        array2 = array1.reshape(3, 3)
        print(array2)
        array2 = np.pad(array2, pad_width=1, mode='constant', constant_values=0)
        print("After using pad fun add zero at border:")
        print(array2)

    @staticmethod
    def checkerboard_matrices():
        array1 = np.zeros((8, 8), dtype= int)
        print("Original array:")
        print(array1)
        array1[1::2, ::2] = 1
        array1[::2, 1::2] = 1
        print("checkerboard pattern:")
        print(array1)

    @staticmethod
    def list_tuple_array():
        list1 = [1, 2, 3, 4, 5, 6, 7, 8]
        print("Original List:", list1)
        arr = np.array(list1)
        print("After convert list to array:", arr)
        # Using second built in function(asarray)
        # arr1 = np.asarray(list1)
        # print(arr1)
        tuple1 = ((8, 4, 6), (1, 2, 3))
        print("Original Tuple:", tuple1)
        # array2 = np.array(tuple1)
        # print("After convert Tuple to array:",array2)
        array3 = np.asarray(tuple1)
        print("After convert Tuple to array:")
        print(array3)

    @staticmethod
    def append_end_array():
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        print("Original array:")
        print(arr)
        print("After append values to the end of the array:")
        list2 = np.append(arr, [9, 10, 11])
        print(list2)

    @staticmethod
    def complex_array():
        x = np.sqrt([1.00000000 + 0.j])
        y = np.sqrt([0.70710678 + 0.70710678j])
        print("Original array x: ", x)
        print("Original array y: ", y)
        print("Real part of the array:")
        print("Real value of x:", x.real)
        print("Real value of y:", y.real)
        print("Imaginary part of the array:")
        print("Img value of x:", x.imag)
        print("Img value of y:", y.imag)

    @staticmethod
    def len_array():
        ele_arr = np.array([20, 12, 23, 84, 95, 100, 989, 1200], dtype=np.float)
        print("Element of array:", ele_arr)
        print("Size of the Arr: ")
        print(ele_arr.size)
        print("Length of one array element in bytes: ")
        print(ele_arr.itemsize)
        print("Total bytes consumed by the elements of the array: ")
        print(ele_arr.nbytes)

    @staticmethod
    def common_array():
        arry1 = np.array([20, 12, 23, 84, 95, 100, 989, 120], dtype=np.int)
        print("First Array:", arry1)
        arry2= np.array([500, 12, 84, 10, 22, 55, 78, 95, 100], dtype=np.int)
        print("Second Array:", arry2)
        print("Common value bet two array:")
        comm_arr = np.intersect1d(arry1, arry2)
        print(comm_arr)

    @staticmethod
    def diff_array():
        arry1 = np.array([1210, 12, 23, 84, 95, 20, 989, 120], dtype=np.int)
        print("First Array: ", arry1)
        arry2 = np.array([500, 12, 84, 10, 22, 55, 78, 95, 989, 100], dtype=np.int)
        print("Second Array: ", arry2)
        print("Diff bet two array,Unique values in array1 that are not in array2:")
        diff_array = np.setdiff1d(arry1, arry2)
        diff_array = np.sort(diff_array)
        print(diff_array)

    @staticmethod
    def set_exclusive_array():
        arry1 = np.array([10, 20, 30, 40, 50, 60], dtype=np.int)
        print("First Array: ", arry1)
        arry2 = np.array([30, 50, 40, 80], dtype=np.int)
        print("Second Array: ", arry2)
        print("Unique values in that are in only one (not both) of the input arrays:")
        set_exclusive_array = np.setxor1d(arry1, arry2)
        set_exclusive_array = np.sort(set_exclusive_array)
        print(set_exclusive_array)

    @staticmethod
    def compare_array():
        arry1 = np.array(input('Enter first array:').split(","), dtype=np.int)
        print("First Array: ", arry1)
        arry2 = np.array(input('Enter Second array:').split(","), dtype=np.int)
        print("Second Array: ", arry2)
        print("First_arr > Sec_arr: ", np.greater(arry1, arry2))
        print("First_arr >= Sec_arr: ", np.greater_equal(arry1, arry2))
        print("")
        print("First_arr < Sec_arr: ", np.less(arry1, arry2))
        print("First_arr <= Sec_arr: ", np.less_equal(arry1, arry2))


# NumpyBasics.list_one_dim_array()common_array
# NumpyBasics.matrices_reshape()
# NumpyBasics.null_vector()
# NumpyBasics.reverse_numpy()
# NumpyBasics.two_d_border()
# NumpyBasics.add_zero_border()
# NumpyBasics.checkerboard_matrices()
# NumpyBasics.list_tuple_array()
# NumpyBasics.append_end_array()
# NumpyBasics.complex_array()
# NumpyBasics.len_array()
# NumpyBasics.common_array()
# NumpyBasics.diff_array()
# NumpyBasics.set_exclusive_array()
# NumpyBasics.compare_array()


