class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substrings = []
        for x in range(len(s)):
            count = 1
            check = []
            check.append(s[x])
            i = x + 1
            while i < len(s) and s[x] != s[i] and s[i] not in check:
                check.append(s[i])
                count += 1
                i += 1
            substrings.append(count)
        return max(substrings)
        
