class Solution(object):
    def findJudge(self, n, trust):
        inc={}
        out={}
        if not trust and n>1:
            return -1
        if not trust and n==1:
            return n
        for i in range(len(trust)):
            if trust[i][0] not in out:

                out[trust[i][0]]=1
            else:
                 out[trust[i][0]]+=1



            if trust[i][1] not in inc:

                inc[trust[i][1]]=1
            else:
                 inc[trust[i][1]]+=1

        for i,j in inc.items():
            if j==n-1 and i not in out :
                return i

        return -1

    




                

        