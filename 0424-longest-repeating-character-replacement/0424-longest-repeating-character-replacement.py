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
            
            max_f = max(count.values())

            if (r - l + 1) - max_f <= k:
                res = max(res, r - l + 1)
                r += 1
                continue

            while l <= r:
                count[s[l]] -= 1
                l += 1
                
                max_f = max(count.values())
                if (r - l + 1) - max_f <= k:
                    break
            
            r += 1
            
        return res






