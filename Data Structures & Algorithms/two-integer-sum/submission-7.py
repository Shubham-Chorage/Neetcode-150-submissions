class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for index, num in enumerate(nums):
            to_find = target - num
            if to_find in dictionary:
                return [dictionary[to_find],index]

            dictionary[num] = index