class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = len(columnTitle) - 1
        for c in columnTitle:
            ans += 26**n * (ord(c) - ord("A") + 1)
            n -= 1
        return ans