class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued   = self.queue[0]
            del self.queue[0]
            
            return dequeued

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
            
        return self.queue[0]