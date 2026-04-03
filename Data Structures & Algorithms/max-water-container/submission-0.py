class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0
        end = len(heights)-1
        curr_amount = 0
        max_amount = 0

        while start < end:
            curr_amount = min(heights[start], heights[end]) * (end - start)
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
            max_amount = max(max_amount, curr_amount)

        return max_amount