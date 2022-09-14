class MinStack:
    # # 1. 辅助栈 O(1) O(N)

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min_stack = []


    # def push(self, val: int) -> None:
    #   self.stack.append(val)
    #   if not self.min_stack or val <= self.min_stack[-1]:
    #     self.min_stack.append(val)


    # def pop(self) -> None:
    #   if self.stack.pop() == self.min_stack[-1]:
    #     self.min_stack.pop()


    # def top(self) -> int:
    #   return self.stack[-1]


    # def getMin(self) -> int:
    #   return self.min_stack[-1]

    # 2. 保存差值，不用额外空间 O(1) O(1)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = float('inf')


    def push(self, val: int) -> None:
      if not self.stack:
        self.min_value = val
      diff = val - self.min_value
      self.stack.append(diff)
      self.min_value = min(val, self.min_value)

    def pop(self) -> None:
      p = self.stack.pop()
      if p < 0:
        self.min_value = self.min_value - p

    def top(self) -> int:
      top = self.stack[-1]
      if top < 0:
        return self.min_value
      else:
        return top + self.min_value

    def getMin(self) -> int:
      return self.min_value