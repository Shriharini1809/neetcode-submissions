class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        list1 = []
        for i in s:
            list1.append(i)
        right = len(s) - 1
        while left < right:
            if list1[left] == list1[right]:
                left+=1
                right-=1
                continue
            else:
                temp1 = list1.copy()
                temp1.pop(left)
                st1=''.join(temp1)

                temp2 = list1.copy()
                temp2.pop(right)
                st2=''.join(temp2)

                if st1==st1[::-1] or st2==st2[::-1]:
                    return True
                else:
                    return False
        return True
