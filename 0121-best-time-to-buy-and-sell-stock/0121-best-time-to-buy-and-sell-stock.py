class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        max_prof=0
        while r<len(prices):

            max_prof=max(max_prof,(prices[r]-prices[l]))
            if prices[l]>=prices[r]:
                l=r


            r+=1

        return max_prof
        