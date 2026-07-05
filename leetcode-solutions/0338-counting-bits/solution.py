class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            count = 0
            current_num = i
            while current_num:
                current_num = current_num &(current_num-1)
                count+=1
            result.append(count)
        return result
