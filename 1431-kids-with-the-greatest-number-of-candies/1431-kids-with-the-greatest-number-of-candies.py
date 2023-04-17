class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= _max)
        return result