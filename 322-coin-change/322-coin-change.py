class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(amnt):
            if amnt < 0:
                return float('inf')
            if amnt == 0 :
                return 1
            minn = float('inf')
            for coin in coins:
                temp = dp(amnt - coin)
                minn = min(minn, temp)
            
            return minn + 1
        ans = dp(amount)
        return ans -1 if ans != float('inf') else -1
      
                
                
                
                