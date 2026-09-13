class Solution(object):
    def productExceptSelf(self, nums):

        out=[]
        pre=1
        for i in  range(len(nums)):
            out.append(pre)
            pre=nums[i]*pre

        post=1
        for i in range(len(nums)-1,-1,-1):
            out[i]*=post
            post=nums[i]*post

        return out






        