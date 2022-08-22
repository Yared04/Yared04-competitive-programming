class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 0
        for weight in weights:
            left = max(left,weight)
            right += weight
        while left <= right:
            mid = (left + right)//2
            day = 1
            weight = 0
            for w in weights:
                if w + weight > mid:
                    day += 1
                    weight = 0
                weight += w
            if day <= days:
                right = mid -1
            else:
                left = mid + 1
        return left