from collections import namedtuple

class PriorityQueue:
    Element = namedtuple("element", ["priority", "data"])

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False
    
    def enqueue(self, priority, data):
        return self.queue.append(PriorityQueue.Element(priority, data))

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        data = self.queue[0]
        idx  = 0

        for i in range(1, len(self.queue)):
            if data.priority < self.queue[i].priority:
                data = self.queue[i]
                idx  = i
        
        del self.queue[idx]
        
        return data

