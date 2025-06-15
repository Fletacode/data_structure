from typing import Optional, Iterable


class Node(Iterable):
    def __init__(self, data: Optional[int] = None, link=None) -> None:
        self.data = data
        self.link: Optional["Node"] = link

    def __repr__(self) -> str:
        return f"node:{self.data}"

    # def __iter__(self):
    #     return self.NodeIterator(self)
    #
    # class NodeIterator:
    #     def __init__(self, node):
    #         self.current = node
    #
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         if self.current is None:
    #             raise StopIteration
    #         node = self.current
    #         self.current = self.current.link
    #         return node

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.link



def explore(node):
    while node is not None:
        print(f"({node})", end="->")
        node = node.link
    print("\b\b")


def build(size):
    node = None
    for i in range(size - 1, -1, -1):
        node = Node(i, node)
    return node


class ListLinkedSingly:
    def __init__(self) -> None:
        self.tail_: Optional[Node] = None
        self.head_: Optional[Node] = None

    def empty(self):
        return self.head_ is None or self.tail_ is None

    def insert_head(self, data: int) -> None:
        node = Node(data)
        if self.empty():
            self.head_ = node
            self.tail_ = node
        else:
            node.link = self.head_
            self.head_ = node

    def insert_tail(self, data: int) -> None:
        node = Node(data)
        if self.empty():
            self.tail_ = node
            self.head_ = node
        else:
            self.tail_.link = node
            self.tail_ = node

    def head(self):
        if self.empty():
            return None
        return self.head_.data

    def tail(self):
        if self.empty():
            return None
        return self.tail_.data

    def __repr__(self):
        temp = []
        node = self.head_
        while node is not None:
            temp.append(node.data)
            node = node.link
        return str(temp)

    # def __iter__(self):
    #     return self.NodeIterator(self)

    # class NodeIterator:
    #     def __init__(self, node):
    #         self.current = node
    #
    #     def __next__(self):
    #         if self.current is None:
    #             raise StopIteration
    #         now = self.current
    #         self.current = self.current.link
    #         return now

    def insert(self, tgt:int, data:int) -> None:

        find_node = None
        prev_node = None

        if self.head_.data == tgt:
            node = Node(data, self.head_.link)
            self.head_.link = node
            return

        # find node
        for item in self.head_:
            if item.data == tgt:
                node = Node(data,item.link)
                item.link = node
                return

    def delete(self, tgt:int):
        prev_node = None
        next_node = None

        if (self.head_.data == tgt):
            self.head_ = self.head_.link
            return


        for item in self.head_:
            if item.link.data == tgt:
                find_node = item.link
                prev_node = item
                next_node = item.link.link
                break

        prev_node.link = next_node

def info(list_: ListLinkedSingly) -> None:
    print(f"list{list_.head(), list_.tail()} = {list_}")


if __name__ == "__main__":
    llist = ListLinkedSingly()
    info(llist)
    llist.insert_tail(20)
    info(llist)
    llist.insert_head(10)
    info(llist)
    llist.insert_tail(40)
    info(llist)
    llist.insert(20, 30)
    info(llist)
    llist.insert(10, 15)
    info(llist)
    llist.delete(10)
    info(llist)

    llist.delete(40)
    info(llist)
    llist.delete(20)
    info(llist)
    llist.delete(15)
    info(llist)
    llist.delete(30)
    info(llist)
    llist.insert_head(10)
    info(llist)
    llist.insert_tail(40)
    info(llist)




