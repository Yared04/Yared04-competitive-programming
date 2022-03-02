class Solution:
    def check(self, target, weights):
        ptr = count = 0
        while ptr < len(weights):
            total = 0
            if weights[ptr] <= target:
                while ptr < len(weights) and total + weights[ptr] <= target:
                    total += weights[ptr]
                    ptr += 1      
            else:
                return 50001  
            count += 1
        return count
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       
        left = 1
        total_weight = sum(weights)
        right = total_weight
        while left <= right:
            mid = (left + right)//2
            if math.ceil(total_weight/days) > mid:
                left = mid + 1
            else:
                if self.check(mid, weights) < days:
                    res = mid
                    right = mid -1
                elif self.check(mid, weights) > days:
                    left = mid +1
                else:
                    res = mid
                    right = mid -1
        return res
        