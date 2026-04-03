class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        output = [1]*length

        prefix = suffix = 1

        for num in range(length):
            output[num] = prefix
            prefix *= nums[num]

        for num in range(length-1,-1,-1):
            output[num] *= suffix
            suffix *= nums[num]

        return output