class Solution(object):
    def romanToInt(self, s):
        var=0
       

        for i in range(len(s)):
            if s[i]=='I' and i!=len(s)-1:
                if s[i+1]=="V" or s[i+1]=='X':
                    var-=1
                else:
                    var+=1
            elif s[i]=='I' and i==len(s)-1:
                 var+=1

            if s[i]=="V":
                var+=5
            if s[i]=='X' and i!=len(s)-1:
                if s[i+1]=="L" or s[i+1]=='C':
                    var-=10
                else:
                    var+=10
            elif s[i]=='X' and i==len(s)-1:
                var+=10
            if s[i]=='C' and i!=len(s)-1:
                if s[i+1]=="D" or s[i+1]=='M':
                   var-=100
                else:
                    var+=100
            elif s[i]=='C' and i==len(s)-1:
                var+=100
            if s[i]=='L':
                var+=50
            if s[i]=="D":
                var+=500
            if s[i]=="M":
                var+=1000
        return var


        