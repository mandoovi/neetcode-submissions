class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solve = defaultdict(list) #key = charCount, value = list of amagrams
        
        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            solve[tuple(count)].append(string)

        return solve.values()