
class Solution:
    palindromes = []

    def longPalindrome(self, substring: str) -> str:
        for x in range(0, int(len(substring)/2)):
            if substring[x] != substring[len(substring) - x - 1]:
                return
        self.palindromes.append(substring)
        return

    #print(palindromes)
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for x in range(1, len(s) + 1):
            for i in range(len(s) - x + 1):
                j = i + x -1
                for k in range(i, j+1):
                    result += s[k]
                #print(result)
                self.longPalindrome(result)
                result = ""
        return self.palindromes[len(self.palindromes)]