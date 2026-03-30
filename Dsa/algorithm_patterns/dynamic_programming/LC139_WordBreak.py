class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n

        for i in range(1, n + 1):
          for word in wordDict:
            start = i - len(word)
            if start >= 0 and dp[start] and s[start:i] == word:
              dp[i] = True
              break
        return dp[n]