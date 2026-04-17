class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        result = max(nums)

        max_val = 1
        min_val = 1

        for n in nums:
            
            if n == 0:
                max_val, min_val = 1, 1

            temp = max_val
            max_val = max(n, n * max_val, n * min_val)
            min_val = min(n, n * temp, n * min_val)

            result = max(result, max_val)

        return result
