class Solution(object):
    def maximumWealth(self, accounts):

        maxx=float('-inf')
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
            
            maxx=max(sum,maxx)
        return maxx
        




        