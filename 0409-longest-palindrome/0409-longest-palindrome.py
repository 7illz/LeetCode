class Solution(object):
    def longestPalindrome(self, s):

        if len(s)==1:
            return 1
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=1

            else:
                dic[s[i]]+=1

        count=0
        for i,j in dic.items():
            if j%2!=0:
                count+=1
        if count==0 or count==1:
            return len(s)
        if count>=2:

            return len(s)-count+1

         




        