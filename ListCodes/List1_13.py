class List1:
    def sum(self):
        num_list = [int(y) for y in input("Enter numbers: ").split(",")]

        total = 0
        for y in num_list:
            total = total+y

        print("Sum of list numbers:", total)
        return total


obj = List1()
obj.sum()
