class Solution(object):
    def addDigits(self, num):
        var=str(num)
        if len(var)==1:
            return num
        return self.checkLen(var)



    def checkLen(self,var):
        dig=0
        for i in range(len(var)):
            dig+=int(var[i])
        var=str(dig)
        if len(var)!=1:
            return self.checkLen(var)
        else:
            return int(var)






        