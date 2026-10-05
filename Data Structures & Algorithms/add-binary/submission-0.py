class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        st = ""
        n1 = len(a)
        n2 = len(b)
        while n1 > 0 or n2 > 0:
            if n1 > 0:
                d1 = a[n1 - 1]
            else:
                d1 = 0
            if n2 > 0:
                d2 = b[n2 - 1]
            else:
                d2 = 0
            sum = carry + int(d1) + int(d2)
            remainder= sum % 2
            quo = sum // 2
            carry = quo
            st += str(remainder)
            n1 = n1 - 1
            n2 = n2 -1
        if carry == 1:
            st += str(carry)
        return st[::-1]
