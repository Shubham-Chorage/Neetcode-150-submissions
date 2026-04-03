class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        zero_count = nums.count(0)

        if zero_count > 1:
            output = [0]*len(nums)
            return output
        else:
            output = [1]*len(nums)
            start = start2 = 1

        for num in nums:
            start2 *= num
            if num != 0:
                start *= num

        position = 0
        for i in nums:
            if i == 0:
                output[position] = start
            else:
                output[position] = int(start2//i)
            position += 1

        print(start)
        print(start2)
        
        return output