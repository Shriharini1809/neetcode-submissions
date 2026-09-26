class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = []
        for i in range(n+1):
            binary = bin(i)
            c = binary.count('1')
            list1.append(c)

        return list1