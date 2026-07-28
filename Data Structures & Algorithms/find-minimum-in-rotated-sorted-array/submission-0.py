class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp < rp:
            mid_index = (lp + rp) // 2

            if nums[mid_index] > nums[rp]: 
                lp = mid_index + 1
            else:
                rp = mid_index

        return nums[lp]