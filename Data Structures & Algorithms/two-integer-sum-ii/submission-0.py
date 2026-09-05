class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []
        n = len(numbers)
        
        left = 0
        right = n - 1

        while left < right:
            difference = target - numbers[left]
            if numbers[right] == difference:
                return [left + 1, right + 1]
            elif numbers[right] > difference:
                right -= 1
            else:
                left += 1
        
        return []


