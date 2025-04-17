from typing import List, Optional

class ArrayListOrdered:
    def __init__(self, capacity=5):
        self.caacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.cur = 0

    def __repr__(self):
        return str(self.arr)

    def __len__(self):
        return self.cur

    def empty(self):
        return self.cur == 0

    def full(self):
        return self.cur == self.capacity

    def empty(self) -> bool:
        pass
    def full(self) -> bool:
        pass

    def add(self, data:int) -> None:
        #self.arr.sort()
        idx = self.cur
        while 0 < idx and self.arr[idx - 1] > data:
            idx -= 1

        temp = data
        while idx <= self.cur:
            temp, self.arr[idx] = self.arr[idx], temp
            idx += 1
        self.cur += 1

    def search(self, data:int) -> bool:
        idx = 0
        while idx < self.cur and self.arr[idx] != data:
            idx += 1
        return idx < self.cur and self.arr[idx] == data

    def __contains__(self, data: int):
        return self.search(data)

    def clear(self) -> None:
        for i in range(self.cur):
            self.arr[i] = None
        self.cur = 0

    def remove(self, data: int) -> None:
        idx = self.index(data)
        self.cur -= 1
        while idx < self.cur:
            self.arr[idx] = self.arr[idx + 1]
            idx += 1
        self.arr[self.cur] = None
        #self.cur -= 1


    def index(self, data: int) -> int:
        idx = 0
        while self.arr[idx] != data:
            idx += 1
        return idx

    def pop(self, index: int = -1) -> Optional[int]:
        idx = index if index >= 0 else self.cur + index
        #print('test', idx)
        temp = self.arr[idx]
        while idx <= self.cur:
            self.arr[idx] = self.arr[idx + 1]
            idx += 1
        self.cur -= 1
        return temp



if __name__ == "__main__":
    arr = ArrayListOrdered()
    arr.add(5)
    arr.add(3)
    arr.add(4)
    print(arr)
    arr.remove(4)
    print(arr)
    # print(f"arr.pop() = {arr.pop()}")
    # print(f"arr.pop(0) = {arr.pop(0)}")
    # arr.add(10)
    # arr.add(1)
    # print(arr)
    # print(f"arr.pop(-3) = {arr.pop(-3)}")
    # print(arr)
    # print(f"arr.pop(-1) = {arr.pop(-1)}")
    # print(arr)
    # arr.add(5)
    # arr.add(3)
    # arr.add(1)
    # arr.add(2)
    # print(arr)
    # print(f"arr.search(10) = {arr.search(10)}")
    # print(f"arr.search(2) = {arr.search(2)}")
    # print(f"arr.index(3) = {arr.index(1)}")
    # print(f"arr.index(5) = {arr.index(5)}")
    # print(f"arr.has(10) = {10 in arr}")
    # print(f"arr.has(10) = {4 in arr}")
    # arr.remove(1)
    # print(f"arr.remove(1): arr = {arr}")
