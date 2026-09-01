class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        res = []
        var = []
        
        while nums:

            var.append(nums.pop(0))
            

            if len(var) == 2:
                res.append(var[1])  
                res.append(var[0])  
                var = []           
                
        return res


        