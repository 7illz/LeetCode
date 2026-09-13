class Solution(object):
    def longestConsecutive(self, nums):

        numset = set(nums)
        longest = 0
        
        for i in numset:

            if i - 1 not in numset:
                current_length = 1
                
 
                while i + 1 in numset:
                    current_length += 1
                    i += 1
                    
     
                if current_length > longest:
                    longest = current_length
                    
        return longest




   
        