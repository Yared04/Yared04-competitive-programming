class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = min(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for i in range(len(time)):
                total += mid // time[i]
            if total < totalTrips:
                left = mid +1
            else:
                result = mid
                right = mid - 1
        return result
                