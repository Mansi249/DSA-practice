class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == "[":
                stack.append((current_str,num))
                num = 0
                current_str = ""
            elif ch == "]":
                prev_str , repeat = stack.pop()
                current_str = prev_str + repeat*current_str
            else :
                current_str += ch
        return current_str
                 
