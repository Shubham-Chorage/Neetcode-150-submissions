class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        for n, c in count.items():
            heapq.heappush(heap, (-c, n))

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
