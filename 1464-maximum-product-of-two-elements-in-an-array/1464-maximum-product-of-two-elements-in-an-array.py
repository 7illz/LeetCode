class Solution(object):
    def maxProduct(self, nums):
        lar=0
        sec=0
        for i in nums:
            if i >=lar:
                temp=lar
                lar=i
                sec=temp
            elif i > sec:
                sec=i

        return (lar-1) * (sec-1)

        