class Solution(object):
    def searchInsert(self, nums, target):

        left=0
        right=len(nums)-1

        def bin(left, right):
                
                if left > right:
                    return left

                middle = (left + right) // 2

                if nums[middle] == target:
                    return middle

                if target > nums[middle]:
                    return bin(middle + 1, right)

                else:
                    return bin(left, middle - 1)

        return bin(left, right)
        