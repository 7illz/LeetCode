class Solution(object):
    def generate(self, numRows):
        res=[[1]]
        for i in range(numRows-1):
            new=[]
            temp=[0]+ res[-1] +[0]
            for j in range(len(res[-1])+1):
                new.append(temp[j]+temp[j+1])
            res.append(new)
        return res

        