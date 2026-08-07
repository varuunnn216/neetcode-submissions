class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_p = nums[0]
        fast_p = nums[0]

        while True:
            slow_p = nums[slow_p]
            fast_p = nums[nums[fast_p]]

            if slow_p == fast_p:
                break
            
        slow_p2 = nums[0]
        while slow_p2 != slow_p:
            slow_p2 = nums[slow_p2]
            slow_p = nums[slow_p]

        return slow_p