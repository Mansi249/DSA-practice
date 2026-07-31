class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        if len(s)!= len(t):
            return False
        for p,q in zip(s,t):
            if p in hash_map1 and hash_map1[p] != q:
                return False
            if q in hash_map2 and hash_map2[q] != p:
                return False
            hash_map1[p] = q
            hash_map2[q] = p
           
        return True
