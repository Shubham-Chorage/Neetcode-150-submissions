class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length = len(nums)+1
        total_sum = (length*(length-1))//2
        result_sum = 0

        for i in nums:
            result_sum += i

        print(total_sum)
        print(result_sum)

        if result_sum == total_sum:
            return 0
        else:
            return total_sum - result_sum


