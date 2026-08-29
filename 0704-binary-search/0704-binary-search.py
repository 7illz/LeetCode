class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1

        def bin(left,right):

            mid= (left+right)//2

            if left>right:
                return -1

            if target==nums[mid]:
                return mid

            if target>nums[mid]:
                return bin(mid+1,right)


            else:
                return bin(left,mid-1)




        return bin(left,right)

        