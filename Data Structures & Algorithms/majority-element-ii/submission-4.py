class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        list1 = []
        n = len(nums) // 3
        for key,value in d.items():
            if value > n:
                list1.append(key)
        return list1

        
                
