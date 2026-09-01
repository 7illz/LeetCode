class Solution(object):
    def getFinalState(self, nums, k, multiplier):

        for i in range(k):
            idx=-1
            minn=float('inf')
            for j in range(len(nums)):


                if nums[j]<minn:
                    minn=nums[j]
                    idx=j

            nums[idx]=minn*multiplier

        return nums


