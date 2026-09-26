class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        c = binary.count('1')
        return c