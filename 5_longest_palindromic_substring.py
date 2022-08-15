# Solution works but needs to be optimized
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ptr1 = 0
        ptr2 = n
        print(s[ptr1:ptr2])
        while ptr1 != ptr2:
            if self.isPalindrome(s[ptr1:ptr2]):
                return s[ptr1:ptr2]
            ptr2 -= 1
            for i in range(n - ptr2 + 1):
                if self.isPalindrome(s[ptr1:ptr2]):
                    return s[ptr1:ptr2]
                ptr1 += 1
                ptr2 += 1
            ptr2 -= ptr1
            ptr1 = 0
        
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for x in s:
            if x.isalpha() or x.isdigit():
                palindrome += x.lower()
        if palindrome == palindrome[::-1]:
            return True
