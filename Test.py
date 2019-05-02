class Lin_Mul:

    def multi_matrix(self):
        row = int(input("Enter the value row size:"))
        col = int(input("Enter the value col size:"))
        temp = []
        for i in range(row):
            matrix = []
            for j in range(col):
                matrix.append(int(input()))
            temp.append(matrix)

        for r in temp:
            print(r)
        return temp

    def callmuti(self):
        first_matrix =obj.multi_matrix()
        second_matrix = obj.multi_matrix()
        # print(first_matrix, second_matrix)

obj = Lin_Mul()
# obj.multi_matrix()
obj.callmuti()

