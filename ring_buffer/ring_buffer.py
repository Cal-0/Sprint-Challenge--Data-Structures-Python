from collections import deque


class RingBuffer:
  
    def __init__(self, capacity):
        self.capacity = capacity 
        self.queue = deque()
        self.length = 0
        self.oldest = 0

    def append(self, item):
            if self.length + 1 <= self.capacity:
                self.length += 1
                self.oldest += 1
                self.queue.append(item)
            else:
                if self.oldest + 1 <= self.capacity - 1:
                    self.oldest += 1
                else:
                    self.oldest = 0
                self.queue[self.oldest] = item
            
            



    def get(self):
        list = [x for x in self.queue if x is not None]
        return list