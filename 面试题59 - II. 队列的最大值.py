import collections


class MaxQueue:

    # 1. 单调双向队列 O(1) O(N)

    def __init__(self):
        self.queue = collections.deque()
        self.deque = collections.deque()
        
    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.popleft()
        if val == self.deque[0]:
            self.deque.popleft()
        return val
