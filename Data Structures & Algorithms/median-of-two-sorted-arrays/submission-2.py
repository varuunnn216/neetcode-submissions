class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total_left = (m + n + 1) // 2

        lp = 0
        rp = m

        while lp <= rp:
            part1 = (lp + rp) // 2
            part2 = total_left - part1

            left1 = nums1[part1 - 1] if part1 > 0 else float('-inf')
            right1 = nums1[part1] if part1 < m else float('inf')
            left2 = nums2[part2 - 1] if part2 > 0 else float('-inf')
            right2 = nums2[part2] if part2 < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                rp = part1 - 1
            else:
                lp = part1 + 1

        return 0.0
        