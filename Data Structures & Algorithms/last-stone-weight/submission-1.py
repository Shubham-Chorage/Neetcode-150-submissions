import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -(heapq.heappop(max_heap))
            large = -(heapq.heappop(max_heap))

            heapq.heappush(max_heap,-abs(largest-large))

        return -max_heap[0]