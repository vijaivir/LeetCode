class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for x in s:
            if x.isalpha() or x.isdigit():
                palindrome += x.lower()
        
        if palindrome == palindrome[::-1]:
            return True
