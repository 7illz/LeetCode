class Solution(object):
    def reverseWords(self, s):

        s=s.split()
        var=''
        for i in range(len(s)):
            if i!=len(s)-1:
                var+=s[i][::-1]+' '
            else:
                 var+=s[i][::-1]

        return var


        