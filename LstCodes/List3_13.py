class List3:
    def sum(self):
        num_list = [int(y) for y in input("Enter numbers: ").split(",")]
        min_no = min(num_list)
        print(min_no)

    def minno(self):
        num_list = [int(y) for y in input("Enter numbers: ").split(",")]

        minn = num_list[0]
        for num in num_list:
            if num < minn:
                minn = num

        print("Min No is:", minn)


obj = List3()
obj.minno()
