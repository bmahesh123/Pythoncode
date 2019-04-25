class List2:
    def sum(self):
        num_list = [int(y) for y in input("Enter numbers: ").split(",")]

        total = 1
        for y in num_list:
            total = total*y

        print("Multiplication of list numbers:", total)
        return total


obj = List2()
obj.sum()
