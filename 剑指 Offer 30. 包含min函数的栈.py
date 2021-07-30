class MinStack:
    # 辅助栈 空间换时间 不同步
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)            

    def pop(self) -> None:
        if self.data.pop() == self.helper[-1]:
            self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.helper[-1]