class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getSquareValue(n)

        return n == 1

    def getSquareValue(self,n):

        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit*digit
            n //= 10

        return sum
