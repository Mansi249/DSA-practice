from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap = []
        count_map = Counter(s)
        for char,freq in count_map.items():
            heapq.heappush(max_heap,(-freq,char))
            result = []
        while max_heap:
            neg_freq,char = heapq.heappop(max_heap)
            actual_freq = -neg_freq
            result.append(char*actual_freq)

        return "".join(result)
