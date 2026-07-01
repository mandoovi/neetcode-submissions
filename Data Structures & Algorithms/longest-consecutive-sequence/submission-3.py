class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums_set:
            length = 0
            current = num
            
            while current in nums_set:
                length += 1
                current += 1

            longest_length = max(length, longest_length)

        return longest_length