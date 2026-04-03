class Solution:
    def isHappy(self, n: int) -> bool:

        # Floyd's Approach / Fast and Slow Pointers

        def getNextN(n):

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            return total

        slow = n
        fast = getNextN(n)

        while fast != 1 and slow != fast:
            slow = getNextN(slow)
            fast = getNextN(getNextN(fast))

        return fast == 1
        