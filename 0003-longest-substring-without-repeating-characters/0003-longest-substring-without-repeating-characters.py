class Solution(object):
    def lengthOfLongestSubstring(self, s):

        newset=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in newset:
                newset.remove(s[l])
                l+=1

            newset.add(s[i])

            res= max(res,i-l+1)
        return res 