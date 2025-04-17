from typing import Optional, List


class ArrayListOrdered:
    def __init__(self, capacity=5):
        self.capacity = capacity
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

    def add(self, target):
        if (self.full()):
            raise ValueError('Array is full')

        if (self.empty()):
            self.arr[self.cur] = target
            self.cur += 1
            return

        temp_cur = self.cur
        while (temp_cur > 0 and self.arr[temp_cur - 1] > target):
            temp_cur -= 1

        i = self.cur
        while (i > temp_cur):
            self.arr[i] = self.arr[i - 1]
            i -= 1

        self.arr[temp_cur] = target
        self.cur += 1

    def search(self, target: int) -> bool:
        if (self.empty()):
            return False
        i = self.cur - 1
        while i >= 0:
            if (self.arr[i] == target):
                return True
            i -= 1
        return False

    def __contains__(self, target):
        if (self.empty()):
            return False
        for i in self.arr:
            if (i == target):
                return True
        return False

    def has(self, target: int) -> bool:
        if (self.empty()):
            return False

        if (target in self.arr):
            return True
        return False

    def clear(self):
        self.cur = 0
        self.arr = [None] * self.capacity

    def remove(self, target: int) -> None:
        if (self.empty()):
            raise ValueError('Array is empty')

        idx = self.index(target)
        cur = self.cur - 1

        while cur > idx:
            self.arr[cur-1] = self.arr[cur]
            self.arr[cur] = None
            cur -= 1

    def index(self, target):
        if (self.empty()):
            raise ValueError('Array is empty')

        i = 0
        while (i < self.cur):
            if (self.arr[i] == target):
                return i
            i += 1

        return -1

    def pop(self, index: int = None) -> Optional[int]:
        if (index == None):
            self.cur -= 1
            ret = self.arr[self.cur]
            self.arr[self.cur] = None
            return ret
        else:
            if (index < 0):

                temp = self.arr[self.cur + index]
                arr.remove(self.arr[self.cur + index])
                return temp
            else:
                temp = self.arr[index]
                arr.remove(self.arr[index])
                return temp


if __name__ == '__main__':
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
