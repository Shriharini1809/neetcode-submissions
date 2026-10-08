class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        val = int(s) + 1
        list1 = []
        st = str(val)
        for i in st:
            list1.append(i)
        return list1