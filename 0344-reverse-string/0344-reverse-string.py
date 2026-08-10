class Solution(object):
    def reverseString(self, s):
        
        l=0
        r = len(s) - 1
        while l<r:
            temp=s[r]
            s[r]=s[l]
            s[l]=temp
            r-=1
            l+=1
             
        