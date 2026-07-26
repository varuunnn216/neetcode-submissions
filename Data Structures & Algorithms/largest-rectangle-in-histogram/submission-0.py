class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for current_index in range(len(heights)):
            current_height = heights[current_index]

            while stack and heights[stack[-1]] > current_height:
                bar_index = stack.pop()
                bar_height = heights[bar_index]

                left_b = stack[-1] if stack else -1
                width = current_index - left_b - 1

                area = bar_height * width
                max_area = max(area, max_area)

            stack.append(current_index)

        while stack:
            bar_index = stack.pop()
            bar_height = heights[bar_index]
            left_b = stack[-1] if stack else -1
            width = len(heights) - left_b - 1
            area = bar_height * width
            max_area = max(area, max_area)

        return max_area
        