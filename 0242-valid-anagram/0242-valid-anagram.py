class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=1
            else:
                dic[s[i]]+=1

        for i in range(len(s)):
            if t[i] in dic and dic[t[i]]==1:
                del dic[t[i]]

            elif t[i] in dic and dic[t[i]]>1:
                dic[t[i]]-=1
            elif t[i] not in dic:
                return False
        return True

        