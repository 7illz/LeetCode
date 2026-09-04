class Solution:
    def thirdMax(self, nums):


        
        f=float('-inf')
        s=float('-inf')
        t=float('-inf')

        for i in range(len(nums)):
            if nums[i]>f: 
                temp=f
                f=nums[i]
                var=s
                s=temp
                t=var 
            elif nums[i]>s and f!=nums[i]:
                var=s
                s=nums[i]
                t=var

            elif nums[i]>t and s!=nums[i] and f!=nums[i]:
                t=nums[i]
            
        if t==float('-inf'):
            return f
        return t