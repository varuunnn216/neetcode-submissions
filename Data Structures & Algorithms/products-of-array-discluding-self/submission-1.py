class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_left = [1] * n
        product_right = [1] * n

        for i in range(1, n):
            product_left[i] = product_left[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            product_right[i] = product_right[i+1] * nums[i+1]

        output = [1] * n
        for i in range(n):
            output[i] = product_left[i] * product_right[i]

        return output
        