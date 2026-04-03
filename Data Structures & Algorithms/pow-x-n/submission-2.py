class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Divide into smaller powers 2**4 can also be written as (2**2)**2
        # 2**3 can be written as 2**2 * 2**1

        result = 1
        power = abs(n)

        while power:
            if power % 2 == 1:
                result *= x
            
            x *= x
            power //= 2

        return result if n >= 0 else 1/result
            