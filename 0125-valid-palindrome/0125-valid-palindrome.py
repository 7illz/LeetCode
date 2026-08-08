class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        valid='abcdefghijklmnopqrstuvwxyz0123456789'
        j=len(s)-1
        i=0
        while i<j:
            while i<j and  s[j]   not in valid:
                j-=1

            while i<j and  s[i]  not in valid:
                i+=1
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

        

        