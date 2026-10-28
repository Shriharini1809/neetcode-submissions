class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr = nums[::-1]
        if k > len(nums):
            k = k % len(nums)
        list1 = arr[:k]
        list1 = list1[::-1]
        list2 = nums[0:len(nums)-k]
        for i in range(len(list1)):
            nums[i] = list1[i]
        for i in range(len(list2)):
            nums[k+i] = list2[i]
        return nums
        