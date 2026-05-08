class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        length = len(nums)
        number = nums[0]
        count = 0

        for num in nums[1:]:
            if num == number:
                count += 1
            elif num != number and count == 0:
                number = num

        return number
        