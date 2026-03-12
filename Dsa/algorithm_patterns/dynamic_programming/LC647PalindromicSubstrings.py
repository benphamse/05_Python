class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def expand(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt

        ans = 0
        for i in range(n):
            ans += expand(i, i)
            ans += expand(i, i + 1)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("abc"))
    print(s.countSubstrings("aaa"))