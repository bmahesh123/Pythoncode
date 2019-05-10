import numpy as np
from numpy.linalg import inv

class Lin_Alg:

    @staticmethod
    # Addition of matrix
    def addmet(self):

        X = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]

        Y = [[48, 8, 1],
             [6, 7, 3],
             [4, 5, 9]]

        result = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

        for i in range(len(X)):
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]
        for r in result:
            print(r)

        # result = np.add(X,Y)
        # print(result)


    # Scalar multiplication of matrix
    @staticmethod
    def scalarMat():
        for i in range(No):
            for j in range(No):
                mat[i][j] = mat[i][j] * k

        print("Scalar Matrix is : ")
        for i in range(No):
            for j in range(No):
                print(mat[i][j], end=" ")
            print()


        # res = np.dot(mat, k)
        # print(res)


# Multiplication of matrix
    @staticmethod
    def multiplication_mat():
        matrix1 = [[12, 7, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        matrix2 = [[5, 8, 1],
                  [6, 7, 3],
                  [4, 5, 9]]

        res = [[0 for x in range(3)] for y in range(3)]
        # print(res)

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
        for m in res:
            print(m)

    @staticmethod
    def inverse_mat():
        matrix1 = [[12, 7, 3],
                    [4, 5, 6],
                    [7, 8, 9]]

        result = np.linalg.inv(matrix1)

        for i in result:
            print(i)


# input parameter for 2nd code *********** start**********
No = 3
mat = [[1, 2, 3],
[4, 5, 6],
[7, 8, 5]]
k = 4
# ******** End *******************


# Lin_Alg.addmet()
# Lin_Alg.scalarMat()
# Lin_Alg.multiplication_mat()
Lin_Alg.inverse_mat()

