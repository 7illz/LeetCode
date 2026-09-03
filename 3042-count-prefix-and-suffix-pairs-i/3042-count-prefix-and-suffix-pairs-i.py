class Solution(object):
    def countPrefixSuffixPairs(self, words):





        def isPrefixAndSuffix(str1, str2):
            if len(str1)>len(str2):
                return False

            if str1==str2[:len(str1)] and str1==str2[-len(str1):]:
                return True

            else:
                return False






        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                var= isPrefixAndSuffix(words[i],words[j])
                if var:
                        count+=1

        return count


             
