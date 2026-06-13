class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        l = 0
        r = 0
        while r<len(s)and l<len(g):
            if g[l]<=s[r]:
                l +=1
                r+=1
            else:
                r+=1
        return l
