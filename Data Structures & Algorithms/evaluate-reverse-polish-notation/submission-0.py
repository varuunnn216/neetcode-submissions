class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                second_op = stack.pop()
                first_op = stack.pop()

                if token == '+':
                    result = first_op + second_op
                elif token == '-':
                    result = first_op - second_op
                elif token == '*':
                    result = first_op * second_op
                else:
                    result = int(first_op / second_op)
                
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]