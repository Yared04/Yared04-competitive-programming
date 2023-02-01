class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def countWhites(start, end):
            count = 0
            for i in range(start, end + 1):
                if blocks[i] == 'W':
                    count += 1
            return count
        i = 0
        j = k - 1
        ans = 101
        while j < len(blocks):
            ans = min(ans, countWhites(i, j))
            i += 1
            j += 1
        return ans
            