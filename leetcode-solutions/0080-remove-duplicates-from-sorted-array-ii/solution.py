class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for x in nums:
            if j<2 or x!= nums[j-2]:
                nums[j] = x
                j+=1
        return j
