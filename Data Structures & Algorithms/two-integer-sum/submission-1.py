class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i, value in enumerate(nums):
            diff = target - value
            if diff in checker:
                return [checker[diff], i]
            checker[value] = i