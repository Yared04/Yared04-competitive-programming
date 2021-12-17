def maxCoins(piles) -> int:
    start = len(piles)-2
    end = len(piles)//3 -1
    output = 0
    piles.sort()
    for i in range(start, end, -2):
        output += piles[i]
    return output

piles = [2,4,5]
print(maxCoins(piles))
        