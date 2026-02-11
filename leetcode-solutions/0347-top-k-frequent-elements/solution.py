from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        min_heap = []
        for number,frequency in count_map.items():
            heapq.heappush(min_heap,(frequency,number))
            if len(min_heap) >k:
                heapq.heappop(min_heap)
        return [pair[1] for pair in min_heap]
