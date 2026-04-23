class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        check = [0] * 26

        if len(s) != len(t):
            return False

        for ch in range(len(s)):
            check[ord(s[ch]) - ord('a')] += 1
            check[ord(t[ch]) - ord('a')] -= 1

        return all(c == 0 for c in check)