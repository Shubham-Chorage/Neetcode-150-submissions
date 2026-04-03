class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = set()
        left = 0
        right = 0
        max_seq = 0

        while right < len(s):
            if s[right] not in result:
                result.add(s[right])
                right += 1
                max_seq = max(max_seq,right-left)

            else:
                result.remove(s[left])
                left += 1
        
        return max_seq

        