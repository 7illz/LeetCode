class Solution(object):
    def minWindow(self, s, t):
        d1 = {} 
        d2 = {}
        for i in t:
            if i not in d1:  
                d1[i] = 1
                d2[i] = 0
            else:
                d1[i] += 1

        need = len(d1) 
        have = 0
        l, r = 0, 0
        res = [-1, -1]    
        lenght = float('inf')

        while r < len(s):
            if s[r] in t:
                d2[s[r]] += 1
                if d2[s[r]] == d1[s[r]]:
                    have += 1
            
            if have == need:
                if r - l + 1 < lenght:    
                    res = (l, r)
                    lenght = r - l + 1
                
                while l <= r:           
                    if s[l] in t:
                        d2[s[l]] -= 1
                        if d2[s[l]] < d1[s[l]]:  
                            have -= 1
                            l += 1
                            break
                        else:
                            if r - l < lenght:    
                                res = (l + 1, r)     
                                lenght = r - l
                                
                    else:
                        if have == need:
                            if r - l < lenght:
                                res = (l + 1, r)
                                lenght = r - l
                    
                    l += 1
        
            r += 1
            
        if res[0] == -1:   
            return ''
        return s[res[0]:res[1]+1]