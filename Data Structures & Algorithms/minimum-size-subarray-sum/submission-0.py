class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 100000
        total_sum = nums[0]
        if total_sum >= target:
            return 1

        left = 0
        right = 1

        while right < len(nums):
            total_sum += nums[right]
            while total_sum >= target:
                min_length = min(right - left + 1, min_length)
                total_sum -= nums[left]
                left += 1
            right += 1


        return 0 if min_length == 100000 else min_length