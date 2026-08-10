class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        dic={}
        for i in range(len(pattern)):
            if len(s)!=len(pattern):
                return False
            if pattern[i] not in dic.keys():
                if s[i]  in dic.values() :
                    return False 
                
                dic[pattern[i]]=s[i]
            else:
                if dic[pattern[i]]!=s[i]:
                    return False
        return True


