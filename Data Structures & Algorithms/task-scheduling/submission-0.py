from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_heap = []
        count = Counter(tasks)
        result = []

        for task, freq in count.items():
            heapq.heappush(task_heap,-freq)

        time = 0

        while task_heap:
            cycle = 0
            temp = []

            for i in range(n+1):
                if task_heap:
                    freq = heapq.heappop(task_heap)
                    if freq + 1 < 0:
                        temp.append(freq + 1)
                    cycle += 1
                else:
                    break

            for item in temp:
                heapq.heappush(task_heap, item)

            if task_heap:
                time += (n+1)
            else:
                time += cycle


        return time
            





