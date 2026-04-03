class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output =[]
        length = len(intervals)
        i = 0

        while i < length and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < length and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        output.append(newInterval)

        while i < length:
            output.append(intervals[i])
            i += 1

        return output