class Solution(object):
    def divisorGame(self, n):
        dp={}
        dp[1]=False
        dp[2]=True
        for i in range(3, n+1):
            if i%2!=0:
                dp[i]= not dp[i-1]

            else:
                dp[i]=not dp[i-1] or not dp[i-2]

        return dp[n]



