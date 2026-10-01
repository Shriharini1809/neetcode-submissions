class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        result = 0
        for i in d:
            if d[i] > 1:
                result = i
        return result
