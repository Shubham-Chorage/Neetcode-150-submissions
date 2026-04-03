class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)
        print(unique)

        curr_len = 1
        max_len = 0
        
        for num in unique:
            if num - 1 not in unique:
                curr_len = 1
                curr = num
                while curr + 1 in unique:
                    curr += 1
                    curr_len += 1
                max_len = max(curr_len, max_len)
        
        return max_len