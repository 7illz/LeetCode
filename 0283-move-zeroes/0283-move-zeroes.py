class Solution(object):
    def moveZeroes(self, nums):

        l,r=0,0
        while r<len(nums):
            if nums[r]!=0:
                temp=nums[r]
                nums[r]=nums[l]
                nums[l]=temp
                l+=1
            r+=1
        return nums
            
                






            



        