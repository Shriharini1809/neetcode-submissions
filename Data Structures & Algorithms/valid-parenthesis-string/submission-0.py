class Solution:
    def checkValidString(self, s: str) -> bool:
        open_counter = 0
        close_counter = 0
        for i in range(len(s)):
            if s[i] ==  "(" or s[i] == "*":
                open_counter += 1
            else:
                open_counter -=1
            
            if s[len(s)-1-i] == ")" or s[len(s)-1-i] == "*":
                close_counter += 1
            else:
                close_counter -= 1
            
            if open_counter < 0 or close_counter < 0:
                return False
        return True
