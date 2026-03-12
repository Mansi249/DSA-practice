class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s = " ".join(words)
        chars = list(s)
        chars.reverse()
        start = 0
        for i in range(len(s)+1):
            if i == len(chars) or chars[i] ==' ':
                chars[start:i] = reversed(chars[start:i])
                start = i+1
        return "".join(chars)

