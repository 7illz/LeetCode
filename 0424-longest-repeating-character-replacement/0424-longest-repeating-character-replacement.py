class Solution(object):
    def characterReplacement(self, s, k):
        l, r = 0, 0
        res = 0
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0 

        while r < len(s):
            count[s[r]] += 1 
            
            freq=max(count.values())
            if r-l+1 - freq <=k:
                res= max(res,r-l+1)
                r+=1
                continue
            
                
            while l<r:
                   count[s[l]] -= 1
                   l+=1
                   freq=max(count.values())
                   
                   if r-l+1 -freq <=k: 
                       r+=1
                       break
                       
                     
                       
            

        return res
             