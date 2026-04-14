class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_value = {}
        for i in range(len(s)):
            char = s[i]
            last_value[char] = i

        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            char = s[i]
            end = max(end, last_value[char])

            if i == end:
                partition_size = end - start + 1
                result.append(partition_size)
                
                start = i + 1

        return result
        