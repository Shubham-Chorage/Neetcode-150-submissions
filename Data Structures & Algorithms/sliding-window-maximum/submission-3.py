from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()  # stores indices
        result = []

        for r in range(len(nums)):

            # 1. Remove smaller elements from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # 2. Add current index
            q.append(r)

            # 3. Remove elements outside window
            if q[0] <= r - k:
                q.popleft()

            # 4. Record result when window is valid
            if r >= k - 1:
                result.append(nums[q[0]])

        return result