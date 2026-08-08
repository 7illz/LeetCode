class Solution(object):
    def majorityElement(self, nums):

        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key,value in dic.items():
            if value>len(nums)/2:
                return key


        