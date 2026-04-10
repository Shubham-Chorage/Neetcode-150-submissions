import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        result = []

        for x,y in points:
            distance = x*x + y*y
            heapq.heappush(heap,(-distance,[x,y]))

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            result.append(heapq.heappop(heap)[1])

        return result



