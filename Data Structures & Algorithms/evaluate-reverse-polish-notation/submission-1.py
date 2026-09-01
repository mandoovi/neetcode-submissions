class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                val_1 = stack.pop()
                val_2 = stack.pop()
                final = val_1 + val_2
                stack.append(final)
            elif val == '-':
                val_1 = stack.pop()
                val_2 = stack.pop()
                final = val_2 - val_1
                stack.append(final)
            elif val == '*':
                val_1 = stack.pop()
                val_2 = stack.pop()
                final = val_1 * val_2
                stack.append(final)
            elif val == '/':
                val_1 = stack.pop()
                val_2 = stack.pop()
                final = int(val_2 / val_1)
                stack.append(final)
            else:
                stack.append(int(val))
        
        return stack.pop()
            
            
