class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string_s = {}
        string_t = {}

        
        for char in s:
            if char in string_s:
                string_s[char] += 1
            else:
                 string_s[char] = 1
        
        for char in t:
            if char in string_t:
                string_t[char] += 1
            else:
                 string_t[char] = 1


        return string_s == string_t