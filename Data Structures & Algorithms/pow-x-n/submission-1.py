class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = 1
        power = abs(n)

        while power:
            if power % 2:
                result *= x

            x *= x
            power //= 2

        return result if n >= 0 else 1/result

