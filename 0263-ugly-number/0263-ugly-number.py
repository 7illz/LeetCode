class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False

        lst=[2,3,5]
        i=0

        var=n
        while i<3:
            if var%lst[i]==0:
                var=var//lst[i]
            else:
                i+=1
                
            if var==1:
                return True
        return False


        