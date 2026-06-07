class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min_value = float('inf')
        while low<=high:
            mid = (high+low)//2
            if nums[mid]>=nums[low]:
                min_value = min(min_value,nums[low])
                low = mid+1
            if nums[mid]<=nums[high]:
                min_value = min(min_value,nums[mid])
                high = mid-1
            
        return min_value
