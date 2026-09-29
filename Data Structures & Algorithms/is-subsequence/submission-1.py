class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0

        for i in range(len(s)):
            found = False
            for j in range(start,len(t)):
                if s[i] == t[j]:
                    start = j+1
                    found= True
                    break
            if found == False:
                return False
        return True
                



