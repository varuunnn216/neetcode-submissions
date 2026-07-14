class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        max_water = 0

        while lp < rp:
            width = rp - lp
            water_height = min(heights[rp], heights[lp])
            current_water = width * water_height

            max_water = max(max_water, current_water)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
            
        return max_water