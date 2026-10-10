class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        list1 = []
        for i in range(len(matrix[0])):
            list2 = []
            for j in range(len(matrix)):
                list2.append(matrix[j][i])
            list1.append(list2)
        return list1