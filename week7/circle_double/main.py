from typing import Optional


class Node:
    def __init__(self,data: Optional[int] = None,) -> None:
        self.data = data
        self.rlink: Optional["Node"] = self
        self.llink: Optional["Node"] = self

        def __repr__(self) -> str:
            return f"{self.data}"

class ListLinkedDoublyCircular:
    """Circular Doubly Linked List"""
    def __init__(self) -> None:
        self.header = None
        self.tailer = None
        self.size = 0

    def empty(self):
        if (self.size == 0):
            return True
        return False

    def head(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.header.data

    def tail(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.tailer.data

    def insert_head(self, data) -> None:
        if self.empty():
            new_node = Node(data)
            new_node.rlink = new_node
            new_node.llink = new_node
            self.header = new_node
            self.tailer = new_node
        else:
            new_node = Node(data)
            new_node.rlink = self.header
            new_node.llink = self.tailer
            self.header.llink = new_node
            self.tailer.rlink = new_node
            self.header = new_node
        self.size += 1

    def insert_tail(self, data) -> None:
        if self.empty():
            new_node = Node(data)
            new_node.rlink = new_node
            new_node.llink = new_node
            self.tailer = new_node
            self.header = new_node
        else:
            new_node = Node(data)
            new_node.rlink = self.header
            new_node.llink = self.tailer
            self.tailer.rlink = new_node
            self.header.llink = new_node
            self.tailer = new_node
        self.size += 1

    def insert(self, tgt: int, data: int) -> None:

        now = self.header
        for _ in range(self.size):
            if now.data == tgt:
                new_node = Node(data)
                new_node.rlink = now.rlink
                new_node.llink = now
                now.rlink.llink = new_node
                now.rlink = new_node
                if now == self.tailer:
                    self.tailer = new_node
                self.size += 1

            now = now.rlink

    def delete(self, tgt: int) -> None:
        now = self.header
        for _ in range(self.size):
            if now.data == tgt:
                if self.size == 1:
                    self.header = None
                    self.tailer = None
                else:
                    now.llink.rlink = now.rlink
                    now.rlink.llink = now.llink
                    if now == self.header:
                        self.header = now.rlink
                    elif now == self.tailer:
                        self.tailer = now.llink
                    self.size -= 1
            now = now.rlink

    def __repr__(self) -> str:
        temp = []
        if self.empty():
            return str(temp)
        cursor = self.header
        for _ in range(self.size):
            temp.append(cursor.data)
            cursor = cursor.rlink
        return str(temp)
def info(list_: ListLinkedDoublyCircular) -> None:
    print(f"list{list_.head(), list_.tail()} = {list_}")

if __name__ == "__main__":
    llist = ListLinkedDoublyCircular()
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




