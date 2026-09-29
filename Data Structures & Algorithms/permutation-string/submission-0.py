class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter = defaultdict(int)
        for char in s1:
            counter[char] += 1
        
        window = defaultdict(int)
        for i in range(len(s1)):
            window[s2[i]] += 1
        
        if window == counter:
            return True

        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            left = s2[right - len(s1)]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == counter:
                return True

        return False
