class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [3, 6, 7, 11]
        # k = [1, 2, 3, ..., 11]
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = l + ((r-l)//2)
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                result = min(result, k)
                r = k - 1
            elif hours > h:
                l = k + 1
        return result


                    
            


            