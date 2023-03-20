class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] or flowerbed[i-1] or flowerbed[i+1]:
                continue
            else:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0