class Solution(object):
    def removeDuplicates(self, nums):
        var=float("inf")
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                if nums[i]==var:
                    nums.pop(i)
                    return len(nums)
                return len(nums)
                
            if nums[i]==var:
                nums.pop(i)
            elif nums[i]==nums[i+1]:
                nums.pop(i+1)
                var=nums[i]
                i=i+1

            else:
                i+=1
                
        if len(nums)==2 and nums[0]==nums[1]:
                nums.pop(1)
        return len(nums)





        