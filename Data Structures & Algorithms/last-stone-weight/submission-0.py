import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones = self.breakDown(stones)
        
        return stones[0] if stones else 0

    def breakDown(self,stone_heap):

        result = []
        heapq.heapify(stone_heap)

        while len(stone_heap) > 2:
            result.append(heapq.heappop(stone_heap))

        if len(stone_heap) == 2:
            result.append(abs(stone_heap[0] - stone_heap[1]))
        elif len(stone_heap) == 1:
            result.append(stone_heap[0])

        return result

