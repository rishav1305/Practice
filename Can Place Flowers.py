class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        res = 0
        for i in range(1, len(flowerbed) -1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    res += 1
                    flowerbed[i] = 1
            # print(i, res, flowerbed)

        return res >= n 