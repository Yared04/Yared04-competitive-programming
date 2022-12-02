class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            curr = columnNumber % 26
            columnNumber //= 26
            ans.append(chr(curr + ord('A')))
        ans = ans[::-1]
        return "".join(ans)
            