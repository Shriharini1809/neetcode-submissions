class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        list1=[]
        sorted_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            list1.append(sorted_d[i][0])
        return list1

        
        