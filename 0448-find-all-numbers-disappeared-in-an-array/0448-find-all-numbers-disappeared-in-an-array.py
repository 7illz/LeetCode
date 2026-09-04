class Solution(object):
    def findDisappearedNumbers(self, nums):

        
        for i in range(len(nums)):
                temp=abs(nums[i])-1
                if nums[temp]>0:
                    nums[temp]*=-1



        res=[]

        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)

        return res
