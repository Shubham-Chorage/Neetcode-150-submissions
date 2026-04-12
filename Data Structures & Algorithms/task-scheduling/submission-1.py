from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count =  Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            cycle = 0

            for i in range(n+1):
                if max_heap:
                    freq = heapq.heappop(max_heap)
                    if freq + 1 < 0:
                        temp.append(freq + 1)
                    cycle += 1
                else:
                    break

            for item in temp:
                heapq.heappush(max_heap, item)

            if max_heap:
                time += (n+1)
            else:
                time += cycle

        return time
                    
            
        