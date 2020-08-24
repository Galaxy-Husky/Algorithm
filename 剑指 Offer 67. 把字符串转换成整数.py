class Solution:
    def strToInt(self, str: str) -> int:
        """ # 正则
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31-1), -2**31) """
        s = str.strip()
        if not s:
           return 0
        base, i, sign = 0, 0, 1
        int_max, int_min = 2**31-1, -2**31
        if s[0] == '-':
            sign = -1
        if s[0] in '+-':
            i += 1
        for c in s[i:]:
            if not c.isdigit():
                break
            base = 10 * base + ord(c) - ord('0')
        return max(-base, int_min) if sign == -1 else min(base, int_max)