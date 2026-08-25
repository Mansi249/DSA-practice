class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        i = 0
        while i < len(points):
            if i +1< len(points) and points[i][1] >= points[i+1][0]:
                newpoints = min(points[i][1],points[i+1][1])
                i+=2
                while i <len(points) and newpoints >= points[i][0]:
                    newpoints = min(newpoints,points[i][1])
                    i+=1
                arrows+=1
            else:
                i+=1
                arrows+=1
        return arrows
