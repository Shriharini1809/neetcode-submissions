class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        num_total = 0
        for i in nums:
            num_total += i
        
        return total - num_total