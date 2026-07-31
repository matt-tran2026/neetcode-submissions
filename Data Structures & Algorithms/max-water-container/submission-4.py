class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        r = len(heights) - 1
        
        while l < r:
            dist = r - l
            if heights[l] < heights[r]:
                area = dist * heights[l]
            elif heights[l] > heights[r]:
                area = dist * heights[r]
            else: 
                area = dist * heights[l]

            ans = max(area, ans)

            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return ans
