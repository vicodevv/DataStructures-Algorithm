class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        
        for char in s:
            if char.isalnum():
                reverse += char.lower()
        return reverse == reverse[::-1]