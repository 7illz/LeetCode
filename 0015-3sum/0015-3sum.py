class Solution(object):
    def threeSum(self, nums):
        res = []
        num = sorted(nums)
        
        for i in range(len(num)):
           
            if i > 0 and num[i] == num[i-1]:
                continue
                
            l = i + 1
            r = len(num) - 1
            
            while l < r:
                total = num[i] + num[l] + num[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    
                    res.append([num[i], num[l], num[r]])
                    
                   
                    l += 1
                    

                    while l < r and num[l] == num[l-1]:
                        l += 1
                        
        return res