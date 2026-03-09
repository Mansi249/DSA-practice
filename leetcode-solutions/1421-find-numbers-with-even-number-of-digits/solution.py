class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            s = str(num)
            length = len(s)
            if length%2 ==0:
                count+=1

        return count 
