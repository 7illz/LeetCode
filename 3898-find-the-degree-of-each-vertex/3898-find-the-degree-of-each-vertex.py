class Solution(object):
    def findDegrees(self, matrix):
        res=[]
        for i in range(len(matrix)):
            var=0
            for j in range(len(matrix[i])):
                var+=matrix[i][j]

            res.append(var)

        return res




        