from typing import Optional, List

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev = None
        self.next = None

class ListLinkedDoublyCircular:
    """Circular Doubly Linked List"""
    def __init__(self) -> None:
        self.header = None
        self.trailer = None
        self.size = 0

    def empty(self) -> bool:
        return self.size == 0

    def head(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.header

    def tail(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.trailer

    def insert_head(self, data) -> None:
        new_node = Node(data)
        if self.empty():
            self.header = new_node
            self.trailer = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.header
            new_node.prev = self.trailer
            self.header.prev = new_node
            self.trailer.next = new_node
            self.header = new_node
        self.size += 1

    def insert_tail(self, data) -> None:
        new_node = Node(data)
        if self.empty():
            self.header = new_node
            self.trailer = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.trailer
            new_node.next = self.header
            self.trailer.next = new_node
            self.header.prev = new_node
            self.trailer = new_node
        self.size += 1

    def insert(self, tgt: int, data: int) -> None:
        """target node 뒤에 insert 한다."""
        if self.empty():
            self.insert_head(data)
            return

        current = self.header
        for _ in range(self.size):
            if current.data == tgt:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                if current == self.trailer:
                    self.trailer = new_node
                self.size += 1
                return
            current = current.next

    def delete(self, tgt: int) -> None:
        """target node 를 삭제한다."""
        if self.empty():
            return

        current = self.header
        for _ in range(self.size):
            if current.data == tgt:
                if self.size == 1:
                    self.header = None
                    self.trailer = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.header:
                        self.header = current.next
                    if current == self.trailer:
                        self.trailer = current.prev
                self.size -= 1
                return
            current = current.next

    def __repr__(self) -> str:
        if self.empty():
            return "[]"
        
        result = []
        current = self.header
        for _ in range(self.size):
            result.append(str(current.data))
            current = current.next
        
        return "[" + ", ".join(result) + "]"

def info(list_: ListLinkedDoublyCircular) -> None:
    if list_.head():
        head_data = list_.head().data
    else:
        head_data = None
        
    if list_.tail():
        tail_data = list_.tail().data
    else:
        tail_data = None
        
    print(f"list({head_data}, {tail_data}) = {list_}")

if __name__ == "__main__":
    llist = Lisllist = ListLinkedDoublyCircular()
    info(llist)
    llist.insert_tail(30)
    info(llist)
    llist.insert_tail(40)
    info(llist)
    llist.insert_head(20)
    info(llist)
    llist.delete(20)
    info(llist)
    llist.delete(40)
    info(llist)
    llist.insert_head(20)
    info(llist)
    llist.insert(30, 40)
    info(llist)
    llist.insert_tail(50)
    info(llist)
    llist.insert(30, 35)
    info(llist)
    llist.insert(20, 25)
    info(llist)
    llist.delete(20)
    info(llist)
    llist.delete(25)
    info(llist)
    