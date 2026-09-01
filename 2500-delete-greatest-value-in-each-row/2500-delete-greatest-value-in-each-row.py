class Solution(object):
    def deleteGreatestValue(self, grid):
        result=0
        while grid[0]:
            
            boss=float('-inf')
            for i in range(len(grid)):
                maxx=float('-inf')
                max_idx = -1

                for j in range(len(grid[i])):
                    if grid[i][j]>maxx:
                        maxx=grid[i][j]
                        max_idx = j

                grid[i].pop(max_idx)
                boss=max(boss,maxx)

           
            result+=boss
        return result