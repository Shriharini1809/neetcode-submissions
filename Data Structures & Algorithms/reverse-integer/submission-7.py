class Solution:
    def reverse(self, x: int) -> int:
        st = str(x)
        if len(st) == 1:
            if x == 1:
                return x
            if x == 0:
                return x
            return 0
        if x > 0:
            st = st[::-1]
            if int(st) > -2 ** 31 and int(st) < 2 ** 31 -1:
                if st[0] == '0':
                    return int(st[1::])
                else:
                    return int(st)
            else:
                return 0
        else:
            st = st[1::]
            st = st[::-1]
            if int(st) > -2 ** 31 and int(st) < 2 ** 31-1:
                return -int(st)
            else:
                return 0
        return 0