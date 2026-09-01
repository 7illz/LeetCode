class Solution(object):
    def luckyNumbers(self, matrix):
        res=[]
        col=[]
        row=[]
        for i in range(len(matrix)):
            m=float('inf')

            for j in range(len(matrix[i])):
                if matrix[i][j]<m:
                    m=matrix[i][j]
            row.append(m)   
               
        for i in range(len(matrix[i])):
            m=float('-inf')

            for j in range(len(matrix)):
                if matrix[j][i]>m:
                    m=matrix[j][i]
            col.append(m)

        for i in row:
            if i in col:
                res.append(i)

        return res   

         
