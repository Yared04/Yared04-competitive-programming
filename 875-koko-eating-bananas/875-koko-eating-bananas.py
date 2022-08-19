class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for banana in piles:
                hours += ceil(banana/mid)
            if hours <= h:
                right = mid-1
                res = mid
            else:
                left = mid+1
        return  res