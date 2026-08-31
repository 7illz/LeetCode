class Solution(object):
    def findCenter(self, edges):

        dic={}

        for i in range(len(edges)):
            
            # Replaced i[0] with edges[i][0]
            if edges[i][0] not in dic:
                dic[edges[i][0]]=1
            else:
                dic[edges[i][0]]+=1

            # Replaced i[1] with edges[i][1]
            if edges[i][1] not in dic:
                dic[edges[i][1]]=1
            else:
                dic[edges[i][1]]+=1
        count=float('-inf')
        var=0
        for i,j in dic.items():

            if j>count:
                count=j
                var=i

        return var


