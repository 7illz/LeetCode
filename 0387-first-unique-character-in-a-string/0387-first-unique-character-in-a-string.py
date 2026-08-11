class Solution(object):
    
    def firstUniqChar(self, s):
        var=''
        dic={}
        for i in range(len(s)):
            if s[i] not in dic :
                if s[i] not in var: 
                    dic[s[i]]=i
            else:
                var+=s[i]
                del dic[s[i]]
        if len(dic)==0:
            return -1
        low=float ('inf')    
        for i in dic.values():
            if i<low:
                low=i
        return low

        