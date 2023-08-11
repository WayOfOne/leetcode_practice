
# store all the opening parentheses in a stack and pop them out when a closing parentheses is encountered
# if the closing parentheses does not match the opening parentheses, return False
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in pairs:
                first = stack.pop() if stack else '#'
                if pairs[i] != first:
                    return False
            else:
                stack.append(i)
        return not stack