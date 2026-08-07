class Solution(object):
    def longestCommonPrefix(self, strs):
        common=''


        for i in range (len(strs[0])):

            for j in strs:
                if i==len(j) or   j[i] !=strs[0][i] :
                   
                    return common

            common+=j[i]
        return common




        