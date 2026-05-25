class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) -1
        maxL = height[l]
        maxR = height[r]
        vol = 0
        # formula: vol += min(maxL, maxR) - height[i]
        while l < r:
            if maxL < maxR: # if maxL less than maxR
                l += 1
                maxL = max(height[l], maxL)
                vol += maxL - height[l]
            else: # if maxR less than or equal to maxL
                r -= 1
                maxR = max(height[r], maxR)
                vol += maxR - height[r]
        return vol





            