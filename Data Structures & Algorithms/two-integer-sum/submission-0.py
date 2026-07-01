class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference in previous:
                return [previous[difference], i]
            previous[j] = i
