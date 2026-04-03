class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for i, num in enumerate(nums):
            find = target - num

            if find in dictionary:
                return[dictionary[find],i]
            
            dictionary[num] = i