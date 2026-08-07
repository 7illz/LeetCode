class Solution(object):
    def removeDuplicates(self, nums):
        left=1
        right=1

        while right<len(nums):
          if nums[right]==nums[right-1]:
            right+=1
          else:
            nums[left]=nums[right]
            left+=1    
            right+=1
        return left





        