class Solution(object):
    def detectCapitalUse(self, word):
        # l,r=0,len(word)
        # if len(word)==1:

        #     return True
        # while l<r:

        #     if l==0 and chr(ord('A'))<=word[l]<=chr(ord('Z')):

        #         l+=1
        #         if l==1 and chr(ord('A'))<=word[l]<=chr(ord('Z')):
        #             while l<r:
        #                 if chr(ord('a'))<=word[l]<=chr(ord('z')):
        #                     return False
        #                 l+=1
        #         if l==1 and chr(ord('a'))<=word[l]<=chr(ord('z')):
        #             while l<r:
        #                 if chr(ord('A'))<=word[l]<=chr(ord('Z')):
        #                     return False
        #                 l+=1
        #     elif l==0 and chr(ord('a'))<=word[l]<=chr(ord('z')):
        #         l+=1
        #         while l<r:
        #             if chr(ord('A'))<=word[l]<=chr(ord('Z')):
        #                 return False
        #             l+=1
        #     return True
        count=0
        ind=0
        l,r=0,len(word)
        while l<r:
            if chr(ord('A'))<=word[l]<=chr(ord('Z')):
                count+=1
                ind=l
            l+=1

        if count==0:
            return True

        if count==len(word):
            return True

        if count==1 and ind==0:
            return True

        return False

        

        




                

        