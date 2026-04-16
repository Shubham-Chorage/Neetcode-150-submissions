class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.robber(nums[1:]), self.robber(nums[:-1]))

    def robber(self, n):

        a = 0
        b = 0

        for i in range(len(n)):
            a, b = b, max(b, n[i] + a)

        return b


