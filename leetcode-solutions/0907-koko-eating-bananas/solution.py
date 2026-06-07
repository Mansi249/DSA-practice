from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_bananas = float('inf')
        def reqTime(arr,hourly):
            total_hours = 0
            for i in arr:
                total_hours += ceil(i/hourly)
            return total_hours
                

        while high>=low:
            mid = (high+low)//2
            hours_used = reqTime(piles,mid)
            if hours_used<=h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


