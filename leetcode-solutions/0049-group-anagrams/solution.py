from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s :
                index = ord(char) - ord('a')
                count[index] +=1
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values())
