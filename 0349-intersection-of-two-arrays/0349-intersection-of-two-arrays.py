class Solution(object):
    def intersection(self, nums1, nums2):

        # lst=[]
        # new=[]
        # for i in range(len(nums1)):
        #     if nums1[i] not in lst:
        #         lst.append(nums1[i])

        # for i in range(len(nums2)):
        #     if nums2[i] in lst:
        #         lst.remove(nums2[i])
        #         new.append(nums2[i])

        # return new



        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        values = set(nums1)
        result = set()

        for number in nums2:
            if number in values:
                result.add(number)

        return list(result)
