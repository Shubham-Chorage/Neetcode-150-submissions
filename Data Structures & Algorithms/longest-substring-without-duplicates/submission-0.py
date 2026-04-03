class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = set()
        left = 0
        right = 0
        max_seq = 0
        curr_seq = 0

        while right < len(s):
            if s[right] not in result:
                curr_seq += 1
                result.add(s[right])
                right += 1
            elif s[right] in result:
                result.remove(s[left])
                left += 1
                curr_seq -=1
                
            max_seq = max(max_seq,curr_seq)
        
        return max_seq

        