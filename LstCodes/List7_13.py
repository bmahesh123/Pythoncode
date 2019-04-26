class List7:

    '''
    # Use swap concept

    list1 = [10,20,40,50,60,80,100]
    temp = list1
    copy_list2 = list(list1)
    copy_list2 = temp
    print("List1 data: ", list1)
    print("copy_list2 data:",copy_list2)'''

    '''
    list1 = [10, 20, 40, 50, 60, 80, 100]
    copy_list2 = list(list1)
    print("List1 data: ", list1)
    print("copy_list2 data:", copy_list2)
    '''

    # Using Built-in method copy().

    def Cloning(list1):
        list_copy = []
        list_copy = list1.copy()
        return list_copy

        # Driver Code

    list1 = [400, 80, 22, 15, 155, 180]
    list2 = Cloning(list1)
    print("Original List:", list1)
    print("After Cloning:", list2)
