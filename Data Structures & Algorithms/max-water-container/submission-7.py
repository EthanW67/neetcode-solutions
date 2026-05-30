class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 
        maxVal = 0
        while left <= right:
            if heights[left] < heights[right]:
                maxVal = max(maxVal, min((heights[left], heights[right])) * (right - left))
                left += 1
            else:
                maxVal = max(maxVal, min((heights[left], heights[right])) * (right - left))
                right -= 1

        return maxVal