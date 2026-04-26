class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = float('-inf')

        for num in nums:
            if nums.count(num) > len(nums) // 2 and nums.count(num) > majority:
                majority = num

        return majority
