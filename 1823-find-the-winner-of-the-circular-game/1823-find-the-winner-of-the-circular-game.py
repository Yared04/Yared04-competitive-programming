class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1
        players = [i for i in range(1,n+1)]
    #     def winner(idx):
    #         if len(players) == 1:
    #             return players[0]
    #         toRemove = (idx + k) % len(players)
    #         del players[toRemove]
    #         return winner(toRemove)
        
        while len(players) > 1:
            for i in range(k):
                players.append(players.pop(0))
            players.pop(0)
        return players[0]

