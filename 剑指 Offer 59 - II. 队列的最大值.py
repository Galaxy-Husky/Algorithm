import queue

class MaxQueue:
    # 双端队列 + 单调队列

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)
        
    def pop_front(self) -> int:
        if not self.deque:
            return -1
        res = self.queue.get()
        if res == self.deque[0]:
            self.deque.popleft()
        return res
        


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()