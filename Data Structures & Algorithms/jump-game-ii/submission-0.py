class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        curr_max = 0
        curr_end = 0

        for i in range(len(nums) - 1):
            curr_max = max(curr_max, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = curr_max

        return jumps
