class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n-1):
            val1 = ord(s[i]) - ord('a') + 1 
            val2 = ord(s[i+1]) - ord('a') + 1
            total += abs(val1-val2)
        return total