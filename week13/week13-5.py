#week13-5.py
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.now = 1
        self.s = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            self.s.remove(self.heap[0])
            return heappop(self.heap)

        self.now += 1
        return self.now - 1

    def addBack(self, num: int) -> None:
        if num < self.now and num not in self.s:
            self.s.add(num)
            heappush(self.heap, num)

