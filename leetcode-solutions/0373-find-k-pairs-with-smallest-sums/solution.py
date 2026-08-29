import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        res = []
        min_heap = []
        for i in range(min(len(nums1),k)):
            current_sum = nums1[i] + nums2[0]
            heapq.heappush(min_heap,(current_sum,i,0))
        while min_heap and len(res) < k:
            current_sum, i ,j = heapq.heappop(min_heap) 
            res.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                next_sum = nums1[i]+ nums2[j+1]
                heapq.heappush(min_heap,(next_sum,i,j+1))
        return res
