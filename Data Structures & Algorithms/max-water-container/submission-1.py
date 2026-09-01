class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curArea = 1
        maxArea = 0

        while l < r:
            curArea = min(heights[l], heights[r]) * (r - l)
            if curArea > maxArea:
                maxArea = curArea
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea
