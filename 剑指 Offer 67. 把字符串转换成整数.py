import re

min_value, max_value = -2**31, 2**31-1

class Automation:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_num', 'end'],
            'signed': ['end', 'end', 'in_num', 'end'],
            'in_num': ['end', 'end', 'in_num', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_index(self, c):
        if c.isspace():
            return 0
        if c in '+-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_index(c)]
        if self.state == 'in_num':
            self.ans = self.ans*10 + int(c)
            self.ans = min(self.ans, max_value) if self.sign == 1 else min(self.ans, -min_value)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def strToInt(self, str: str) -> int:
        # # 1. 正则
        # return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), max_value), min_value)

        # # 2. 去除空格0->判断正负->ord转换数字->判断溢出 O(N) O(1)
        # if not str:
        #     return 0
        # i = 0
        # while str[i] == ' ':
        #     i += 1
        #     if i == len(str):
        #         return 0
        # base = 0
        # sign = -1 if str[i] == '-' else 1
        # if str[i] in '+-':
        #     i += 1
        # for c in str[i:]:
        #     if not '0' <= c <= '9':
        #         break
        #     digit = ord(c) - ord('0')
        #     if base > max_value // 10 or base == max_value // 10 and digit > max_value % 10:
        #         return max_value if sign == 1 else min_value
        #     base = 10 * base + digit
        # return base * sign

        # 3. DFA O(N) O(1)

        # # 3.1
        # auto = Automation()
        # for c in s:
        #     auto.get(c)
        # return auto.sign * auto.ans

        # 3.2
        states = [
            {' ': 0, 's': 1, 'd': 2},
            {'d': 2},
            {'d': 2, ' ': 3},
            {' ': 3}
        ]

        cur = 0
        t = ''
        sign = 1
        res = 0
        for c in str:
            if c == ' ':
                t = c
            elif c in '+-':
                t = 's'
            elif '0' <= c <= '9':
                t = 'd'
            else:
                t = '?'
            if t not in states[cur]:
                break
            if t == 's':
                sign = 1 if c == '+' else -1
            if t == 'd':
                digit = ord(c) - ord('0')
                if res > max_value // 10 or res == max_value // 10 and digit > max_value % 10:
                    return max_value if sign == 1 else min_value
                res = res * 10 +  digit
            cur = states[cur][t]
        return res * sign
        