class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dic={}
        res=[0] * len(nums1)
        for i in range(len(nums1)):
            dic[nums1[i]]=i


        for i in range(len(nums2)):
            if  nums2[i] in dic:
                for j in range(i+1,len(nums2)):
                    if nums2[i]<nums2[j]:
                        res[dic[nums2[i]]]=nums2[j]
                        break
                if res[dic[nums2[i]]]==0:
                    res[dic[nums2[i]]]=-1
        return res