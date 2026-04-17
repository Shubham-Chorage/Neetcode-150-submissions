class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        n = len(s)
        dp[0] = True
        
        for i in range(1, n+1):
            for word in wordDict:
                L = len(word)

                if i >= L and dp[i - L] and s[i - L: i] == word:
                    dp[i] = True
                    break

        return dp[n]
            