from typing import Iterable


class Array(Iterable):
    def __init__(self, capacity=10, fill=None):
        self.capacity = capacity
        self.fill = fill
        self.data = [fill for _ in range(capacity)]
        self.cursor = 0
        self.iter_idx = capacity - 1

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

    def add(self, other):
        if self.cursor >= self.capacity:
            self.capacity += 1
            temp = [self.fill for _ in range(self.capacity)]
            for i, value in enumerate(self.data):
                temp[i] = value
            temp[self.cursor] = other
            self.data = temp
        else:
            self.data[self.cursor] = other
        self.cursor += 1

    def insert(self, index, value):
        self.add(None)
        i = len(self.data) - 1
        while i > index:
            self.data[i] = self.data[i - 1]
            i -= 1
        self.data[i] = value

    # def __iter__(self):
    #     self.iter_idx = 0
    #     return self
    #
    # def __next__(self):
    #     if self.iter_idx == self.capacity:
    #         raise StopIteration
    #     ret = self.data[self.iter_idx]
    #     self.iter_idx += 1
    #     return ret

    def __iter__(self):
        idx = 0
        while idx < self.capacity:
            yield self.data[idx]
            idx += 1

    def __sum__(self):
        sum_val = 0
        for i in self.data:
            sum_val += i
        return sum_val
        # return sum(self.data)


if __name__ == "__main__":
    SIZE = 5
    arr = Array(SIZE)
    print(arr)

    arr.set(0, 10)
    arr.set(2, 30)
    arr.set(1, 40)
    arr.set(3, 20)
    arr.set(4, 50)

    print(arr)

    arr.add(40)
    arr.add(30)
    arr.add(20)
    arr.add(1)
    arr.add(2)
    arr.add(3)

    print(arr)

    arr.insert(2, 11)

    print(arr)

    for i in arr:
        print(i)

    for idx, val in enumerate(arr):
        print(idx, val)

    print(sum(arr))
