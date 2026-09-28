class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] not in ['+','C','D']:
                stack.append(int(operations[i]))
            elif operations[i] == '+':
                result = 0
                val = -1
                for i in range(2):
                    result += stack[val]
                    val -= 1
                stack.append(result)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                result = 2 * stack[-1]
                stack.append(result)
        fin_result = 0
        for i in range(len(stack)):
            fin_result += stack[i]
        return fin_result