class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(amnt):
            if amnt == 0 :
                return 0
            minn = float('inf')
            for coin in coins:
                if amnt >= coin:
                    minn = min(dp(amnt - coin)+1, minn)
            return minn
        ans = dp(amount)
        return ans if ans != float('inf') else -1
      
                
                
                
                