class Solution(object):
    def getRow(self, rowIndex):
        res=[[1]]
        if rowIndex==0:
            return res[0]
        for i in range(rowIndex):
            temp=[0] + res[-1] +[0]
            new=[]
            for j in range(len(res[-1])+1):
                new.append(temp[j]+temp[j+1])
            res.append(new)
        return res[rowIndex]
        