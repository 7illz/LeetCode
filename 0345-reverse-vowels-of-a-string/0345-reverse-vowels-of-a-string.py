class Solution(object):
    def reverseVowels(self, s):
        l=0
        r=len(s)-1
        s=list(s)
        vowel='aeiouAEIOU'
        while l<r:
            if s[l] in vowel:
                while l<r and s[r] not in vowel:
                    r-=1
                temp=s[r]
                s[r]=s[l]
                s[l]=temp
                r-=1
            l+=1
        
        var = ''.join(s)
        return var
            





        