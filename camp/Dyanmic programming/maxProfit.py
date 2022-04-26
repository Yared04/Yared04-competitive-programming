class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        mini, maxx = prices[0], 0 
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
                maxx = 0 
            elif prices[i] > maxx:
                maxx = prices[i]
            result = max(result,(maxx - mini))
        return result
                