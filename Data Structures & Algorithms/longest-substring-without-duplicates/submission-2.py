class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_seq = 0
        left = 0
        right = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_seq = max(max_seq, right - left)
            else:
                seen.remove(s[left])
                left += 1      

        return max_seq
