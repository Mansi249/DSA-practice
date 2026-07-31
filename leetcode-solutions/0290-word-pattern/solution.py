class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        hash_map1 = {}
        hash_map2 = {}
        for p,q in zip(pattern,words):
            if p in hash_map1 and hash_map1[p]!=q:
                return False
            if q in hash_map2 and hash_map2[q]!= p:
                return False
            hash_map1[p] = q
            hash_map2[q] = p
        return True
