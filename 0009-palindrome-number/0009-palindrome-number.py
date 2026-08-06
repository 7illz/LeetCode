class Solution(object):
    def isPalindrome(self, x):
        sir=str(x)
        j=len(sir )-1
        for i in range(len(sir)):
            if i>j:
                break
            if sir[i]==sir[j]:
                j-=1
            else:
                return False

        return True

        