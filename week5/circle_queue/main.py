from typing import Optional


class QueueCircular:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_ = self.rear_ = 0
    def __len__(self):
        if self.rear_ >= self.front_:
            return self.rear_ - self.front_
        else:
            return (self.capacity - self.front_) + self.rear_
    def empty(self):
        if (self.front_ == self.rear_):
            return True
        return False

    def full(self):
        if (self.arr[(self.rear_+ 1) % self.capacity] != None):
            return True
        return False

    def front(self) -> Optional[int]:
        return self.arr[self.front_+1]
    def rear(self) -> Optional[int]:
        return self.arr[self.rear_]
    def enqueue(self, data):
        if (self.full()):
            raise ValueError('enqueue from full')

        self.rear_ = (self.rear_ + 1) % self.capacity
        self.arr[self.rear_] = data

    def dequeue(self):
        if self.empty():
            raise ValueError('dequeue from empty')

        self.front_ = (self.front_ + 1) % self.capacity
        self.arr[self.front_] = None

    def __repr__(self):
        if (self.rear_ > self.front_):
            return str(self.arr[self.front_+1:self.rear_+1])
        else:
            temp = []
            for i in range(self.front_+1,self.capacity,1):
                temp.append(self.arr[i])
            for i in range(0,self.rear_+1):
                temp.append(self.arr[i])
            return str(temp)
def info_queue(q):
    print(f"queue.cursor:{q.front_, q.rear_}")

    print(f"queue.data:{q.front(), q.rear()}")
    print(f"queue.status:{q.empty(), q.full()}")
    print(f"queue = {q}")
    print(f"queue.size = {len(q)}")

if __name__ == '__main__':
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
    # print(f">> queue.deueue() = {queue.dequeue()}")
    # info_queue(queue)
    # print()
    #
    # print(f">> queue.deueue() = {queue.dequeue()}")
    # info_queue(queue)
    # print()
    # print(f">> queue.deueue() = {queue.dequeue()}")
    # info_queue(queue)
    # print()

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