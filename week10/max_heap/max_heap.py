class TreeBinaryHeapMax:
    def __init__(self):
        self.arr: list[int] = []

    def __repr__(self) -> str:
        return f"{self.arr}"

    def insert(self, elem: int) -> None:
        self.arr.append(elem)
        self.bubble_up()

    # bubble_up
    def delete(self) -> int | None:
        if not self.arr:
            return None

        arr_len = len(self.arr)
        if arr_len == 1:
            return self.arr.pop()

        # Swap root with last element
        self.arr[0], self.arr[arr_len - 1] = self.arr[arr_len - 1], self.arr[0]
        max_elem = self.arr.pop()
        self.bubble_down(0)
        return max_elem

    # bubble_down
    def bubble_up(self) -> None:
        curr_pos = len(self.arr) - 1
        while curr_pos > 0:
            parent_pos = self.parent(curr_pos)
            if self.arr[curr_pos] > self.arr[parent_pos]:
                self.arr[curr_pos], self.arr[parent_pos] = self.arr[parent_pos], self.arr[curr_pos]
                curr_pos = parent_pos
            else:
                break

    def bubble_down(self, pos: int = 0) -> None:
        curr_pos = pos
        heap_size = len(self.arr)

        while True:
            largest_pos = curr_pos
            left_child_pos = self.left(curr_pos)
            right_child_pos = self.right(curr_pos)

            # Check left child
            if left_child_pos < heap_size and self.arr[left_child_pos] > self.arr[largest_pos]:
                largest_pos = left_child_pos

            # Check right child
            if right_child_pos < heap_size and self.arr[right_child_pos] > self.arr[largest_pos]:
                largest_pos = right_child_pos

            # If largest is not the current position, swap and continue down
            if largest_pos != curr_pos:
                self.arr[curr_pos], self.arr[largest_pos] = self.arr[largest_pos], self.arr[curr_pos]
                curr_pos = largest_pos
            else:
                # Heap property is satisfied for this subtree
                break

    def parent(self, pos) -> int:
        # Returns -1 if pos is 0 or invalid to avoid index errors
        return (pos - 1) // 2 if pos > 0 else -1

    def left(self, pos) -> int:
        return 2 * pos + 1

    def right(self, pos) -> int:
        return 2 * pos + 2


# Remove the first, simpler main block if it exists
# // ... existing code ... # Ensure any prior __main__ block is removed or commented out

if __name__ == "__main__":
    print("max heap:")
    input_data = [20, 15, 2, 14, 10] # Renamed from 'input' to avoid shadowing built-in
    heap = TreeBinaryHeapMax()
    for num, elem in enumerate(input_data):
        heap.insert(elem)
        # Use the __repr__ implicitly by passing the object to f-string
        print(f"{num}. inserted: {elem:2d}: {heap}") 
    print()
    
    # Store initial size because heap.arr length changes during deletion
    initial_size = len(heap.arr) 
    for num in range(initial_size):
        deleted = heap.delete()
        # Handle case where delete returns None (shouldn't happen here with proper range)
        deleted_val = deleted if deleted is not None else "N/A" 
        # Use __repr__ implicitly
        print(f"{num}. deleted: {deleted_val:2}: {heap}") 