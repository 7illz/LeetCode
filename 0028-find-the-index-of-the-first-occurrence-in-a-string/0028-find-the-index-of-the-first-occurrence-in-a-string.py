class Solution(object):
    def strStr(self, haystack, needle):
  

        if len(needle)==0:
            return -1

        for i in range(len(haystack)):
            flag=True
            
            if i+len(needle)>len(haystack):
                return -1

            if haystack[i]==needle[0]:
                var=i
                start=i
                
                for j in range(len(needle)):
                        if haystack[start]!=needle[j]:
                            flag=False
                            break              
                        start+=1
                if flag:
                    return var
        return -1
            
                        
        