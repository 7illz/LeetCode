class Solution(object):
    def lemonadeChange(self, bills):
       
        five = 0
        ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1

            if bills[i] == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False

            if bills[i] == 20:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False

        return True

            