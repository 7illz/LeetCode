class Solution(object):
    def toLowerCase(self, s):
        var=[]
        for i in s:
            if chr(ord('A'))<=i<=chr(ord('Z')):
                var.append(chr(ord(i)+32))
            else:
                var.append(i)

        car=''
        for i in var:
            car+=i

        return car


        