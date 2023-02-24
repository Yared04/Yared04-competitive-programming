class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while True:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return ans
                if tickets[i] == 0:
                    continue
                else:
                    tickets[i] -= 1
                    ans += 1
        
            
            