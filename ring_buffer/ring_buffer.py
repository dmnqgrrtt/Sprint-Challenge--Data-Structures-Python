# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.ring = []
#         self.number = 0

#     def append(self, item):
#         self.number += 1
#         if self.number <= self.capacity:
#             self.ring.append(item)
#         else:
#             position = (self.number % self.capacity)
#             if position == 0:
#                 self.ring[self.capacity - 1] = item
#             else:
#                 self.ring[position - 1] = item


#     def get(self):
#         if len(self.ring) > 0:
#             return self.ring
#         else:
#             return []

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.buffer = [None for i in range(self.capacity)]
        

    def append(self, item):
        self.counter += 1
        if self.counter <= self.capacity:
            self.buffer[self.counter - 1] = item
        if self.counter == self.capacity:
            self.counter = 0

    def get(self):
        if self.buffer[0] == None:
            return []
        else:
            return [x for x in self.buffer if x != None]
