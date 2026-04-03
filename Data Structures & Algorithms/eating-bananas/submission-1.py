import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left < right:

            mid = left + (right - left)//2

            if self.canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left

    def canFinish(self,piles, k, h):

        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(pile/k)

        return total_hours <= h
