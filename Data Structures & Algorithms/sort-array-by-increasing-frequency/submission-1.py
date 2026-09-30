class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        list1 = []
        for key,value in sorted(d.items(),key=lambda x:(x[1],-x[0])):
            for _ in range(value):
                list1.append(key)

        return list1           