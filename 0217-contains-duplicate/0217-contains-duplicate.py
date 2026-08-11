class Solution(object):
    def containsDuplicate(self, nums):

        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        flag=False
        for i in dic.values():
            if i >=2:
                flag=True
        return flag