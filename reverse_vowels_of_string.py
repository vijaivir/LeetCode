class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        l = 0
        r = len(slist) - 1
        while l < r:
            if self.isVowel(slist[l]) and self.isVowel(slist[r]):
                slist[l], slist[r] = slist[r], slist[l]
                l += 1
                r -= 1
            elif self.isVowel(slist[l]) and not self.isVowel(slist[r]):
                r -= 1
            elif not self.isVowel(slist[l]) and self.isVowel(slist[r]):
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(slist)
            
    def isVowel(self, v: str) -> bool:
        return v in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
