class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] not in dic.keys():
                dic[nums[i]]=i
            else:
                return [dic[target-nums[i]],i]
                



        
        