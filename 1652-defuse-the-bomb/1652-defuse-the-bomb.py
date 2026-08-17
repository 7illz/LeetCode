class Solution(object):
    def decrypt(self, code, k):


        n=len(code)
       
        l=0
        cur_sum=0
        res=[0] *n
        if k==0:
            return res

        for i in range(n+abs(k)):
            
                cur_sum+=code[i%n]
                if k>0:
                    if i-l==k:
                        cur_sum-=code[l%n]
                        res[l]=cur_sum
                        l+=1

                elif k<0:
                    if i-l==abs(k):
                        cur_sum-=code[l%n]
                        res[(i+1)%n]=cur_sum
                        l+=1

        return res



        # n=len(code)
        # res=[0]*n
        # if k==0:
        #     return res



        # if k>0:
        #     for i in range(n):
        #         for j in range(i+1,i+1+k):
        #             res[i]+=code[j%n]


        # elif k<0:
        #     for i in range(n):
        #         for j in range(i-1,i-1-abs(k),-1):
        #             res[i]+=code[j%n]

        # return res






        