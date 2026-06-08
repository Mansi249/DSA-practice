class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        high1 = m
        low1 = 0
        while high1>=low1:
            mid1 = (low1+high1)//2
            if matrix[mid1][0] <= target<= matrix[mid1][n]:
                high2 = n
                low2 = 0
                while high2>=low2:
                    mid2 = (high2+low2)//2
                    if matrix[mid1][mid2]== target:
                        return True
                    if matrix[mid1][mid2]<target:
                        low2 = mid2+1
                    else:
                        high2 = mid2-1
                return False
            if target > matrix[mid1][0] and target > matrix[mid1][n]:
                low1 = mid1+1
            else :
                high1 = mid1-1
        return False
