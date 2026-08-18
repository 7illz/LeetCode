class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        f=[0] +flowerbed +  [0]
        c=0
        for i in range(1,len(f)-1):
            
            if f[i-1] == 0 and f[i]==0 and f[i+1]==0:
                c+=1
                f[i]=1

        if c>=n:
            return True
        return False

