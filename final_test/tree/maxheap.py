from collections import deque


class TreeBinaryHeadMax:
    def __init__(self):
        self.arr = deque()

    def get_left(self, idx):
        return idx * 2 + 1

    def get_right(self, idx):
        return idx * 2 + 2

    def get_parent(self, idx):
        return (idx - 1) // 2

    def bubbleUp(self):

        now_idx = len(self.arr) - 1

        while now_idx > 0:
            parent_idx = self.get_parent(now_idx)

            if self.arr[now_idx] > self.arr[parent_idx]:
                self.arr[now_idx], self.arr[parent_idx] = (
                    self.arr[parent_idx],
                    self.arr[now_idx],
                )
            now_idx = parent_idx

    def bubbleDown(self):

        now_idx = 0

        while now_idx < len(self.arr):
            max_idx = now_idx
            left = self.get_left(max_idx)
            right = self.get_right(max_idx)

            if left < len(self.arr) and self.arr[left] > self.arr[max_idx]:
                max_idx = left
            if right < len(self.arr) and self.arr[right] > self.arr[max_idx]:
                max_idx = right

            if max_idx == now_idx:
                break

            self.arr[max_idx], self.arr[now_idx] = self.arr[now_idx], self.arr[max_idx]
            now_idx = max_idx

    def insert(self, data):

        self.arr.append(data)
        self.bubbleUp()

    def delete(self):

        if len(self.arr) == 0:
            return 0
        if len(self.arr) == 1:
            return self.arr.pop()

        delete_node = self.arr.popleft()
        self.arr.appendleft(self.arr.pop())
        self.bubbleDown()

        return delete_node

    def __repr__(self):
        return str(self.arr)


if __name__ == "__main__":
    print("max heap:")
    input = [20, 15, 2, 14, 10]

    heap = TreeBinaryHeadMax()

    for i, elem in enumerate(input):
        heap.insert(elem)
        print(f"{i}. inserted: {elem}: {heap}")

    for idx, elem in enumerate(input):
        delete_val = heap.delete()
        print(f"{idx}. deleted: {delete_val}: {heap}")
