class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            if result >= 0:
                result += nums[i]
            else:
                result = nums[i]

            max_sum = max(result,max_sum)
        return max_sum




