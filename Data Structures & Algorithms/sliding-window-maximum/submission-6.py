from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Solve using a queue keep only the max value in queue at top

        q = deque()
        result = []
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1

        return result