class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curr_max = 0
        total_max = 0

        start = 0
        end = len(heights)-1

        while start < end:
            
            min_height = min(heights[start],heights[end])
            curr_max = min_height * (end-start)
            total_max = max(curr_max, total_max)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            


        return total_max