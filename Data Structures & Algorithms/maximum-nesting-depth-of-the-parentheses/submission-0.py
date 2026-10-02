class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max = 0
        count = 0
        for i in s:
            if i == "(":
                stack.append(i)
                count += 1
            elif i == ")":
                stack.pop()
                count -= 1
            else:
                continue
            if count > max:
                max = count
        return max