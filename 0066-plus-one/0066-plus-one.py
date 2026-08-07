class Solution(object):
    def plusOne(self, digits):
        dig=''
        for i in digits:
            dig+=str(i)
        car=int(dig)+1
        var=str(car)
     
        new=[]
        for i in var:
            new.append(int(i))
        return new


        

        


        