class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n= len(citations)
        for i in range(len(citations)):
            total = n-i
            if total<= citations[i]:
                return total
        return 0
