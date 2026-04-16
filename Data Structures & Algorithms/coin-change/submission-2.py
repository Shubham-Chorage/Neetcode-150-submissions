class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.minCoins = float('inf')

        def backtrack(start, total, count):

            if total == amount:
                self.minCoins = min(self.minCoins, count)
                return

            if total > amount:
                return

            if count >= self.minCoins:
                return

            for i in range(start, len(coins)):
                backtrack(i, total + coins[i], count + 1)

        backtrack(0, 0, 0)

        return self.minCoins if self.minCoins != float('inf') else -1