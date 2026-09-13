class Solution(object):
    def topKFrequent(self, nums, k):

        count={}
        freq = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        for i,j in count.items():
            freq[j].append(i)
        res=[]
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:    
                res.append(num)      
                if len(res) == k:    
                    return res
        return res



        
        
