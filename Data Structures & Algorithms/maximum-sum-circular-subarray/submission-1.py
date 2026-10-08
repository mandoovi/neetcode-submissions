class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_max = nums[0]
        total_min = nums[0] 
        
        current_max = 0
        current_min = 0

        running_total = 0

        for num in nums:
            current_max = max(current_max + num, num)
            current_min = min(current_min + num, num)
            
            running_total += num

            total_max = max(total_max, current_max)
            total_min = min(total_min, current_min)

        return max(total_max, running_total - total_min) if total_max > 0 else total_max