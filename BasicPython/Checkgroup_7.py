# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
#
#
# print(is_group_member([1, 5, 8, 3], 5))
# print(is_group_member([5, 8, 3], -1))



def is_list_member(list_value, no):
    print(no)
    print(type(no))
    print(type(list_value[0]))
    for value in list_value:

        if no == value:
            return True
    return False

list = input("Enter List Data:")
print(list)
data = list.split(",")
print(data)
print(is_list_member(data, '2'))
