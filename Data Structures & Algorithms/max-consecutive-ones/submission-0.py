class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current_count = 0
        max_count = 0

        for i, num in enumerate(nums):
            if num == 1:
                current_count += 1
            else:
                current_count = 0
        
            max_count = max(max_count, current_count)

    
        return max_count

                