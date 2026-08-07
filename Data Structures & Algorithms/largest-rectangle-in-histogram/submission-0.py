class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                width = i - index
                area = height * width
                max_area = max(area, max_area)
                start = index
            stack.append((h, start))
        
        while stack:
            height, index = stack.pop()
            width = n - index
            max_area = max(max_area, height*width)
        return max_area
