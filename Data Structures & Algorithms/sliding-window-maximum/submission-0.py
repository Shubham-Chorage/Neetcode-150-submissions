class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        n = len(nums)

        for l in range(n - k + 1):

            max_val = float('-inf')

            for i in range(l, l + k):
                max_val = max(max_val, nums[i])

            result.append(max_val)

        return result

            