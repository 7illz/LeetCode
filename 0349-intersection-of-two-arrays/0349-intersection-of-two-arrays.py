class Solution(object):
    def intersection(self, nums1, nums2):


    

        var=set(nums1)
       

        res=[]
        for i in range(len(nums2)):
            if nums2[i] in var:
                res.append(nums2[i])
                var.remove(nums2[i])

        return res
