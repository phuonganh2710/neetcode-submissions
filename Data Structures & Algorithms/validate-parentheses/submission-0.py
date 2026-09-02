class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charSet = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue

            if c in charSet and stack[-1] == charSet[c]:
                #pop
                stack.pop()
            
            else:
                stack.append(c)
        
        return len(stack) == 0
