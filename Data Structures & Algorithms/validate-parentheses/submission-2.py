class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_pairs = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in matching_pairs:
                if stack and stack[-1] == matching_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
