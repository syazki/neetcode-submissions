class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for bracket in s:
            if stack and stack[-1] == '[' and bracket == ']':
                stack.pop()
            elif stack and stack[-1] == '{' and bracket == '}':
                stack.pop()
            elif stack and stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)
        if not stack:
            return True
        return False