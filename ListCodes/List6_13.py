# Python program to remove duplicates from a list.
# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list
#
#
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))

# adding items into set bcuz set not allowed duplicate

list_dup = [100, 250, 323, 898, 989, 100, 20, 30, 20, 10, 50, 60, 40, 80, 50]
dup_item = set()
print(dup_item)
uni_item = []

for x in list_dup:
    if x not in dup_item:
        uni_item.append(x)
        dup_item.add(x)

# print(uni_item)
print("\n", dup_item)
