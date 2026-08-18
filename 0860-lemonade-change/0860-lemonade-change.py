class Solution(object):
    def lemonadeChange(self, bills):
       
        dic={5:0,10:0}

        for i in range(len(bills)):
            if bills[i]==5:
                dic[5]+=1


            if bills[i]==10:
                dic[10]+=1
                if dic[5]>0:
                    dic[5]-=1
                else:
                    return False

                

            if bills[i]==20:
                if dic[10]>0 and dic[5]>0:
                    dic[5]-=1
                    dic[10]-=1
                elif dic[5]>2:
                    dic[5]-=3

                else:
                    return False

        return True

            