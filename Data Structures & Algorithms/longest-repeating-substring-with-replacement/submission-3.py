class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_len = 0
        left = 0
        right = 0
        dictionary = {}

        while right < len(s):
            char = s[right]
            
            window_size = right - left + 1
            dictionary[char] = dictionary.get(char,0) + 1 
            
            max_freq = max(dictionary.values())

            while (window_size - max_freq) > k:
                dictionary[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            right += 1
            max_len = max(max_len, window_size)

        return max_len
