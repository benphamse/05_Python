class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxLen = 1
        maxStr = s[0]
        s = "#" + "#".join(list(s)) + "#"
        n = len(s)
        dp = [0] * n
        center = 0
        right = 0
        for i in range(1, n):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i + dp[i] < n and i - dp[i] >= 0 and s[i + dp[i]] == s[i - dp[i]]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > maxLen:
                maxLen = dp[i]
                maxStr = s[i - dp[i] + 1:i + dp[i]].replace("#", "")
        return maxStr