class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic={}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[(nums[i])]=i
            else:
                if abs(i-dic[nums[i]])<=k:
                    return True
                else:
                    dic[nums[i]]=i
        return False            





        