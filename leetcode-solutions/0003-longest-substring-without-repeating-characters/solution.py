class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = {}
        start = 0
        max_length = 0
        for x in range(len(s)):
            i = s[x]
            if i in t and t[i]>=start:
                start = t[i]+1
            t[i] = x
            max_length = max(max_length,x-start+1)

        return max_length
