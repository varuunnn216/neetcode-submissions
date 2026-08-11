class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            lp = i + 1
            rp = n - 1
            target = -nums[i]

            while lp < rp:
                cusu = nums[lp] + nums[rp]

                if cusu == target:
                    result.append([nums[i], nums[lp], nums[rp]])

                    lp += 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1

                    rp -= 1
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1

                elif cusu < target:
                    lp += 1
                else:
                    rp -= 1

        return result
        