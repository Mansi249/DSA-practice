class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

