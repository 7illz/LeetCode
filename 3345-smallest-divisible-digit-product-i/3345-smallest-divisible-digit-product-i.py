class Solution(object):
    def smallestNumber(self, n, t):
        
        for i in range(n,101):
            string=str(i)
            car=1

            for j in range(len(string)):
                car=car*int(string[j])
                if car%t==0:
                    return i

 
        