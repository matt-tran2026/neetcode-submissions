class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0 
        maxArea = 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            dist = r - l
            if heights[l] < heights[r]:
                ans = dist * heights[l]
            if heights[l] > heights[r]:
                ans = dist * heights[r]
            if heights [l] == heights[r]:
                ans = dist * heights[l]
            maxArea = max(maxArea, ans)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea