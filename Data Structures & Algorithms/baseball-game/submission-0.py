class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val == '+':
                addition = stack[-1] + stack[-2]
                stack.append(addition)
            elif val == 'D':
                multiply = stack[-1] * 2
                stack.append(multiply)
            elif val == 'C':
                stack.pop()
            else:
                stack.append(int(val))

        total = 0
        for num in stack:
            total += num

        return total