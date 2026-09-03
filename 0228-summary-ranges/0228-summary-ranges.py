class Solution(object):
    def summaryRanges(self, nums):

        if not nums:
            return []
            
        new = []
        count = 0
        start = nums[0] 
        for i in range(len(nums)):
            

            if i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
                count += 1
                
            else:

                if count > 0:
                    new.append(f'{start}->{nums[i]}')
                else:
                    new.append(str(nums[i]))
                
          
                count = 0
                if i < len(nums) - 1:
                    start = nums[i+1] 

        return new



        