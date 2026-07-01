class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        check_s = {}
        check_t = {}

        for char in s:
            check_s[char] = check_s.get(char, 0) + 1

        for char in t:
            check_t[char] = check_t.get(char, 0) + 1

        return check_s == check_t