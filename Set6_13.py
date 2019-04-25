

class Set6:
    set_b = set(["Python", "Java", "Django", "Sql"])
    set_a = set(["Phy", "sci", "Math", "History", "Python"])
   #First Method
    set_inter=set_b & set_a
    print(set_inter)

    # Second Method
    print(set_b.intersection(set_a))

#Third Method

def intersection(lst1, lst2):
    list3 = [value for value in lst1 if value in lst2]
    return list3


set1 = [4, 9, 1, 17, 11, 26, 28, 54]
set2 = [9, 9, 74, 45, 11, 28, 26]
print(intersection(set1, set2))





