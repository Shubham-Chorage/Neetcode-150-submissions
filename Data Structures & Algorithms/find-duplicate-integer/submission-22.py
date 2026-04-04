class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Using set

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)