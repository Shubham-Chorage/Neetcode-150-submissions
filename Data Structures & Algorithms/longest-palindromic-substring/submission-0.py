class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = len(s)
        longest = ""

        for i in range(length):
            for j in range(i+1,length+1):
                curr = s[i:j]
                if curr == curr[::-1] and len(curr) > len(longest):
                    longest = curr

        return longest


