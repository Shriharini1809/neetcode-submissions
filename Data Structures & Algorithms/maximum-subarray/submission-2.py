class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max = nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            cur += nums[i]
            if cur > max:
                max = cur
            if cur < 0:
                cur = 0
        return max