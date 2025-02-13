from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  
                    flowers += 1
            i += 1
        
        return flowers >= n
    
s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1)) 