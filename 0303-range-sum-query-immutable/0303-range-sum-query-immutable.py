class NumArray(object):

    def __init__(self, nums):
        self.prefix=[]
        total=0
        for i in nums:
            total+=i
            self.prefix.append(total)


    def sumRange(self, left, right):
        if left-1<0:
            return self.prefix[right]-0
        return self.prefix[right]-self.prefix[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)