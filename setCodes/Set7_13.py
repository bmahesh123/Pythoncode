
class Set7:
    # First Method
    set_b = set(["Python", "Java", "Django", "Sql"])
    set_a = set(["Phy", "sci", "Math", "History", "Python"])
    print("union value:", set_b.union(set_a))

    # Second Method

    def Union(list1, list2):
        final_list = list1 + list2
        return final_list

    list1 = [15, 2, 14, 14, 16, 20, 52]
    list2 = [48, 15, 12, 26, 32, 47, 54]
    print(Union(list1, list2))


