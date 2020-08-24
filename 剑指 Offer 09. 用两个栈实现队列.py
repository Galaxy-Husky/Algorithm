class CQueue:
    # s1 入栈 s2 出栈
    def __init__(self):
        self.s1, self.s2 = [], []

    def appendTail(self, value: int) -> None:
            self.s1.append(value)

    def deleteHead(self) -> int:
        if self.s2:
            return self.s2.pop()
        if not self.s1:
            return -1
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()