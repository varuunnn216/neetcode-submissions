class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid_index = (lp + rp) // 2
            mid_val = nums[mid_index]

            if mid_val == target:
                return mid_index
            elif mid_val < target:
                lp = mid_index + 1
            else:
                rp = mid_index - 1

        return -1