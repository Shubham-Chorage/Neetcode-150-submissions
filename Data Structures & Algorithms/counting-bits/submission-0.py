class Solution:
    def countBits(self, n: int) -> List[int]:
        
        length = n + 1
        result = [1] * length

        for i in range(0, length):
            result[i] = i.bit_count()

        return result