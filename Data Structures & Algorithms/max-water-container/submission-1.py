class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for l in range(len(heights)):
            for r in range(1,len(heights)):
                width = r-l
                height = min(heights[l], heights[r])
                area = width * height
                if area > maxArea:
                    maxArea = area
       
        return maxArea

            