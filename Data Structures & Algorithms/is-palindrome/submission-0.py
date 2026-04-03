class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(c for c in s if c.isalnum()).lower()
        return cleaned == cleaned[::-1]