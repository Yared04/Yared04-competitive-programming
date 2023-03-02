class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def countHours(speed):
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / speed)
            return hours
            
        
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = low + (high - low) // 2
            if countHours(mid) > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
                