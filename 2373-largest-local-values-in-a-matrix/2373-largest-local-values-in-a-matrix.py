class Solution(object):
    def largestLocal(self, grid):
        n=len(grid)-2
        m=len(grid[0])-2 
        var= [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(n):
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        var[i][j]=max(grid[r][c],var[i][j])

        return var


        

        