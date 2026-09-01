class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0] * n
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stackIndex, StackTemp = stack.pop()
                result[stackIndex] = index - stackIndex

            stack.append((index, temperature))

        return result