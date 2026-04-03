class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = {}
        for num in nums:
            output[num] = nums.count(num)

        sorted_dict = sorted(output.items(), key = lambda item:item[1],reverse = True)
        limit_values = [key for key,value in sorted_dict][:k]
        return limit_values