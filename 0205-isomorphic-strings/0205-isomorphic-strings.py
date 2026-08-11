class Solution(object):
    def isIsomorphic(self, s, t):
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] not in dic.values():

                    dic[s[i]]=t[i]
                else:
                    return False
            else:
                if dic[s[i]]==t[i]:
                    continue
                else:
                    return False
        return True

        