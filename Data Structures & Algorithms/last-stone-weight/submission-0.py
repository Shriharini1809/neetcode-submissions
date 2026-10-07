class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            list1 = sorted(stones,reverse=True)
            if list1[0] - list1[1] > 0:
                val = list1[0] - list1[1]
                stones.append(val)
                stones.remove(list1[0])
                stones.remove(list1[1])
            elif list1[0] == list1[1]:
                stones.remove(list1[0])
                stones.remove(list1[1])
            else:
                continue
        if len(stones) == 0:
            return 0
        return stones[0]