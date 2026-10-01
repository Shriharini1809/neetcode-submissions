class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interset = set()
        for i in nums1:
            if i in nums2:
                interset.add(i)
        return list(interset)