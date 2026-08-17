class Solution(object):
    def decrypt(self, code, k):
        n=len(code)
        res=[0]*n
        if k==0:
            return res



        if k>0:
            for i in range(n):
                for j in range(i+1,i+1+k):
                    res[i]+=code[j%n]


        elif k<0:
            for i in range(n):
                for j in range(i-1,i-1-abs(k),-1):
                    res[i]+=code[j%n]

        return res






        