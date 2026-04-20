from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        need = Counter(t)
        need_len = len(need)
        have = 0
        window = {}
        res = [-1, -1]
        resLen = float('inf')

        l = 0

        for r in range(len(s)):

            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_len:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""

            
        
        