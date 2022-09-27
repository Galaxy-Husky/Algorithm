class MedianFinder:

    # 1. 大根堆+小根堆 O(logN) O(N)
    def __init__(self):
      self.small = []
      self.big = []
      
    def addNum(self, num: int) -> None:
      if len(self.small) != len(self.big):
        heapq.heappush(self.big, -heapq.heappushpop(self.small, num))
      else:
        heapq.heappush(self.small, -heapq.heappushpop(self.big, -num))


    def findMedian(self) -> float:
      if len(self.small) != len(self.big):
        return self.small[0]
      else:
        return (self.small[0] - self.big[0]) / 2

