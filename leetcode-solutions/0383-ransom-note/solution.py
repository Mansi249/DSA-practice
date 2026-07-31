from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        use = Counter(magazine)
        for i in ransomNote:
            if i in use and use[i]>0:
                use[i]-=1
            else:
                return False
        return True
