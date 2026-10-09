class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        max_length = 1
        prev_up = False 

        while right < len(arr):
            cur_up = arr[right - 1] < arr[right]
            if arr[right - 1] != arr[right] and (right - left == 1 or cur_up != prev_up):
                max_length = max(max_length, right - left + 1)
                prev_up = cur_up
                right += 1
            else:
                if arr[right - 1] == arr[right]:
                    right += 1
                left = right - 1

        return max_length