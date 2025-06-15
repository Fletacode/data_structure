class TreeBinaryHeapMax:
    def __init__(self):
        self.arr: list[int] = []
    def insert(self, elem: int) -> None:
        self.arr.append(elem)
        self.bubble_up()

    # bubble_up
    def delete(self) -> int | None:
        if not self.arr:
            return
        
        
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        max_elem = self.arr.pop()
        self.bubble_down()
        return max_elem
    
    # bubble_down
    def bubble_up(self) -> None:
        now = len(self.arr) - 1

        while now > 0:
            next = self.parent(now)
            if self.arr[next] < self.arr[now]:
                self.arr[next], self.arr[now] = self.arr[now], self.arr[next]
            else:
                return
            now = self.parent(now)
        
    def bubble_down(self, pos: int = 0) -> None:
        now = 0
        

        while now < len(self.arr):
            left = self.left(now)
            right = self.right(now)

            if left < len(self.arr) and self.arr[now] < self.arr[left]:
                self.arr[left], self.arr[now] = self.arr[now], self.arr[left]
                now = left
            elif right < len(self.arr) and self.arr[now] < self.arr[right]:
                self.arr[right], self.arr[now] = self.arr[now], self.arr[right]
                now = right
            else:
                return




    def parent(self, pos) -> int:
        return (pos - 1) // 2
    def left(self, pos) -> int:
        return pos * 2 + 1
    def right(self, pos) -> int:
        return pos * 2 + 2

    def __repr__(self) -> str:
        return f"{self.arr}"
    
if __name__ == "__main__":
    print("max heap:")
    input = [20, 15, 2, 14, 10]
    heap = TreeBinaryHeapMax()

    for i in input:
        heap.insert(i)
    #heap.insert(5)
    print(heap.arr)
    size = len(heap.arr)
    for i in range(size):
        maxElem = heap.delete()
        print(maxElem , heap.arr)