class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        d = {}
        for i in nums2:
            d[i] = -1
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                index = stack.pop()
                d[index] = nums2[i]
            stack.append(nums2[i])

        for num in nums1:
            val = d[num]
            result.append(val)
        return result
        