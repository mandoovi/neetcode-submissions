class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output = ""

        for center in range(n):
            left = center
            right = center
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(output):
                    output = s[left:right + 1]
                left -= 1
                right += 1

            left = center
            right = center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(output):
                    output = s[left:right + 1]
                left -= 1
                right += 1

        return output