class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum_val = 0
        left = 0
        
        for right in range(len(nums)):
            sum_val += nums[right]
            
            while sum_val >= target:
                res = min(res, right - left + 1)
                sum_val -= nums[left]
                left += 1
                
        return res if res != float('inf') else 0

                
