class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Approach for word in dictionary 

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                L = len(word)
                if i >= L and dp[i - L] and s[i - L:i] == word:
                    dp[i] = True

        return dp[n]
            