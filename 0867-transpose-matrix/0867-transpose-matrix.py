class Solution(object):
    def transpose(self, matrix):
        rows=len(matrix[0])
        cols=len(matrix)

        new= [[0] * cols for _ in range(rows)]


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new[j][i]=matrix[i][j]


        return new




