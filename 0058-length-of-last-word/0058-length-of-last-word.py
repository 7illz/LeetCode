class Solution(object):
    def lengthOfLastWord(self, s):
        var=s.split()
        return len(var[-1])


        