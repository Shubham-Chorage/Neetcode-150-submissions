class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0
        high = 0

        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == ')':
                low -= 1
                high -= 1
            elif i == '*':
                low -= 1
                high += 1

            low = max(low, 0)
            if high < 0:
                return False

        return low == 0

            



