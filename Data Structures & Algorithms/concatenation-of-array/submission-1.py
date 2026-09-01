class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans is length 2n where each index is equal to each other
        #the start of double the array repeats the exact same values

        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num

        return ans