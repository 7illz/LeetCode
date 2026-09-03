class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l2=n-1
        r1=m-1
        w=m+n-1

        while w>=0:

            if l2<0:
                nums1[w]=nums1[r1]
                r1-=1

            elif r1<0:
                nums1[w]=nums2[l2]
                l2-=1


    	    elif l2>=0 and r1>=0:
                if nums1[r1] >= nums2[l2] :
                    nums1[w]=nums1[r1]
                    
                    r1-=1

                    
                elif nums2[l2]>nums1[r1]:
                    nums1[w]=nums2[l2]
                    l2-=1

            w-=1
        return nums1



