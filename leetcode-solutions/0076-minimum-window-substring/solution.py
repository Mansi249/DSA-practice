class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        left = 0
        right = 0
        count = {}
        window = {}
        res = ""
        minLen = float('+inf')
        for j in t :
            count[j] = count.get(j,0)+1
        need = len(count)
        have = 0
        for right in range(len(s)):
            c = s[right]
            window[s[right]] = window.get(s[right],0)+1
            if c in count and window[c] == count[c]:
                have +=1
            while have == need:
                if (right-left+1) < minLen:
                    minLen = right-left+1
                    res = s[left:right+1]
                window[s[left]] -=1
                if s[left] in count and window[s[left]]<count[s[left]]:
                    have -=1
                left +=1
        return res


                    
                
