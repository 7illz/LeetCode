class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        res=[]
        summ=0
        new=[]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in res:
                    new.append(grid[i][j])
          
                else:
                    summ+=grid[i][j]
                    res.append(grid[i][j])
        n=len(res)+1
        exp= (n*(n+1)) /2
        new.append(exp-summ)

        return new