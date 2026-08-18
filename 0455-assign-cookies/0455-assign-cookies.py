class Solution(object):
    def findContentChildren(self, g, s):
        i,j=0,0
        g.sort()
        s.sort()

        while j<len(s) and i<len(g):
            if g[i]<=s[j]:
                i+=1
            j+=1

        return i

