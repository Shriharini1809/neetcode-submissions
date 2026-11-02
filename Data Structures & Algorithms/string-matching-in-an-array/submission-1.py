class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        string = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] == words[j]:
                    continue
                elif words[i] in words[j]:
                    string.add(words[i])
        sorted_l = sorted(string)
        return sorted_l