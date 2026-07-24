class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+' : lambda y,x: y+x,
            '-': lambda y,x : y-x,
            '*' : lambda y,x : y*x,
            '/' : lambda y,x : int(y/x)
        }
        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[i](a,b)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]
