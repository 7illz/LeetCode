class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        d1 = {}
        d2 = {}
        var = 'abcdefghijklmnopqrstuvwxyz'
        for i in var:
            d1[i] = 0
            d2[i] = 0

        for i in s1:
            d1[i] += 1

        car = len(s1)

        for i in range(car):
            d2[s2[i]] += 1

        if d1 == d2:
            return True

     
        for i in range(car, len(s2)):
            d2[s2[i]] += 1          
            d2[s2[i - car]] -= 1   

            if d1 == d2:
                return True

        return False


        

