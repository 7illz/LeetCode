class Solution(object):
    def findRelativeRanks(self, score):

        res=[]
        dic={}
        for i in range(len(score)):
            dic[score[i]]=i
        score.sort(reverse=True)
        new={}
        for i in range(len(score)):

            var=str(i+1)

            if i ==0:
                var='Gold Medal'

            if i ==1:
                var='Silver Medal'

            if i ==2:
                var='Bronze Medal'

            new[score[i]]=var

        for key in dic:
            res.append(new.get(key,0)) 

        return res
