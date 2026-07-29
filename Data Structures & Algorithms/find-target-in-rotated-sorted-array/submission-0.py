class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid_index = (lp + rp) // 2

            if nums[mid_index] == target:
                return mid_index

            if nums[lp] <= nums[mid_index]:
                if nums[lp] <= target < nums[mid_index]:
                    rp = mid_index - 1
                else:
                    lp = mid_index + 1
            else:
                if nums[mid_index] < target <= nums[rp]:
                    lp = mid_index + 1
                else:
                    rp = mid_index - 1

        return -1
        