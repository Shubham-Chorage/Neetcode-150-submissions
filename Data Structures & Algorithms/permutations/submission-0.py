class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited[i] = False

        backtrack([])
        return result
            