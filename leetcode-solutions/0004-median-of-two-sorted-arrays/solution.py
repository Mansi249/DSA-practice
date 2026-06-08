from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        high1 = len(nums1)
        low1 = 0
        total_elements = (len(nums1)+ len(nums2))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        while high1>=low1 :
            cut1 = (high1+low1)//2
            cut2 = (total_elements+1)//2 - cut1
            l1 = -inf if cut1 == 0 else nums1[cut1-1]
            r1 = inf  if cut1 == len(nums1) else nums1[cut1]
            l2 = -inf if cut2 == 0 else nums2[cut2-1]
            r2 = inf if cut2 == len(nums2) else nums2[cut2]
            if l2>r1:
                low1 = cut1+1
            elif l1>r2:
                high1 = cut1-1
            else :
                if(total_elements%2 ==0):
                    return (max(l1,l2) + min(r1,r2))/2
                else:
                    return max(l1,l2)       

