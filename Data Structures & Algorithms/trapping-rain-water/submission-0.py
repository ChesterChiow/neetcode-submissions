class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) -1
        maxL = height[l]
        maxR = height[r]
        vol = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                vol += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                vol += maxR - height[r]
        return vol





            