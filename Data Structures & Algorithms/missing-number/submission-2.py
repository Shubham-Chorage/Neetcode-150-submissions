class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length = len(nums)
        total_sum = (length*(length+1))//2

        return total_sum - sum(nums)


