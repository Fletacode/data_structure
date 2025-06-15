class QueueCircular:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_ = self.rear_ = 0
    
    def empty(self):
        return self.rear_ == self.front_
    def full(self):
        if len(self) == self.capacity:
            return True
        return False
    
    def front(self):
        if self.empty():
            return None
        return self.arr[self.front_]
    
    def rear(self):
        if self.empty():
            return None
        return self.arr[self.rear_]
    
    def enqueue(self,data):
        if self.full():
            return
        self.arr[self.rear_] = data
        self.rear_ = (self.rear_ + 1) % self.capacity 
        

    def dequeue(self):
        if self.empty():
            return
        self.arr[self.front_] = None
        self.front_ = (self.front_ + 1) % self.capacity

    def __repr__(self):
        return str(self.arr)
    
    def __len__(self):
        if self.rear_ >= self.front_:
            return self.rear_ - self.front_
        else:
            return self.capacity - self.front_ + self.rear_

    
def info_queue(q):
    print(f"queue.cursor:{q.front_, q.rear_}")
    print(f"queue.data:{q.front(), q.rear()}")
    print(f"queue.status:{q.empty(), q.full()}")
    print(f"queue = {q}")
    print(f"queue.size = {len(q)}")
        
if __name__ == "__main__":
    SIZE = 8
    queue = QueueCircular(SIZE)
    print(f"queue = {queue}")
    info_queue(queue)
    print()
    data = "A"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    data = "B"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    data = "C"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    data = "D"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    data = "E"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    data = "F"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    data = "G"
    queue.enqueue(data)
    info_queue(queue)
    print()
    data = "H"
    queue.enqueue(data)
    info_queue(queue)
    print()

    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    data = "J"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()

    data = "I"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()

    print(f">> queue.deueue() = {queue.dequeue()}")
    info_queue(queue)
    print()
    data = "J"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    info_queue(queue)
    print()