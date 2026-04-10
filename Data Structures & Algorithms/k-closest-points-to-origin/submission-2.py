import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        result = []

        for x,y in points:
            distance = x*x + y*y
            heapq.heappush(max_heap, (-distance,[x,y]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        for i in range(len(max_heap)):
            result.append(heapq.heappop(max_heap)[1])

        return result 




