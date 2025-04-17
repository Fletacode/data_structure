import traceback
from typing import List, Optional
class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.front_ = self.rear_ = -1

    def __len__(self):
        return self.rear_ - self.front_

    def __repr__(self) -> str:
        st = self.front_ + 1
        end = self.rear_ + 1
        ret = ", ".join(map(str, self.arr[st: end]))
        return f"[{ret}]"

    # def __repr__(self):
    #     ret = ", ".join(map(str, self.arr[:self.capacity]))
    #     return f"[{ret}]"

    def empty(self) -> bool:
        if (self.rear_ == self.front_):
            return True
        else:
            return False

    def full(self) -> bool:
        if (self.rear_ + 1 == self.capacity):
            return True
        else:
            return False

    def front(self) -> Optional[int]:
        if (self.empty()):
            raise IndexError("front from empty queue")
        else:
            return self.arr[self.front_]

    def rear(self) -> Optional[int]:
        if (self.empty()):
            raise IndexError("rear from empty queue")
        else:
            return self.arr[self.rear_]

    def enqueue(self, data: Optional[int]):
        if (self.full()):
            raise IndexError("enqueue from queue full")

        self.rear_ += 1
        self.arr[self.rear_] = data

    def dequeue(self) -> Optional[int]:
        if (self.empty()):
            raise IndexError("dequeue from empty queue")

        self.front_ += 1
        temp = self.arr[self.front_]
        i = self.front_
        while i < self.rear_:
            self.arr[i] = self.arr[i+1]
            i += 1
        self.rear_ -= 1
        self.front_ -= 1

        return temp

if __name__ == "__main__":
    queue = Queue()
    print(f"queue = {queue.arr}")
    print(f"queue = {queue}")
    print(f"queue.size = {len(queue)}")
    print(f"queue.full() = {queue.full()}")
    print(f"queue.empty() = {queue.empty()}")

    try:
        print(f"queue.front() = {queue.front()}")
    except:
        print(traceback.format_exc())
    try:
        print(f"queue.rear() = {queue.rear()}")
    except:
        print(traceback.format_exc())

    for data in range(10, 60, 10):
        queue.enqueue(data)
        print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")
    print()

    print(f"queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")

    print(f"queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(f"queue = {queue}")
    print(f"queue.info:{queue.front_, queue.rear_} len:{len(queue)}")
    print(f"queue.size() = {len(queue)}")
    print(f"queue.full() = {queue.full()}")
    print(f"queue.empty() = {queue.empty()}")