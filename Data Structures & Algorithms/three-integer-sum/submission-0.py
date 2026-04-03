class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(0, len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums)-1
            target = -nums[i]

            while start < end:
                if nums[start] + nums[end] == target:
                    result.append([nums[i],nums[start],nums[end]])

                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                
                    start += 1
                    end -= 1

                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
            
        return result
            