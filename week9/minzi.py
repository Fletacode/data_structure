from __future__ import annotations
from typing import Optional, List
try:
    from typing import LiteralString
except ImportError:
    try:
        from typing_extensions import LiteralString
    except ImportError:
        LiteralString = str


class TreeBinary:
    class Node:
        def __init__(self, data: Optional[str] = None):
            self.data = data
            self.left: Optional["TreeBinary.Node"] = None
            self.right: Optional["TreeBinary.Node"] = None
        
        def __repr__(self):
            return f"{self.data}"
    
    def __init__(self) -> None:
        self.root: Optional[TreeBinary.Node] = None
    
    def build(self, sexpr: List[LiteralString]) -> None:
        stack: List[TreeBinary.Node] = []
        isRoot = False
        cur: Optional[TreeBinary.Node] = None

        for token in sexpr:
            if token == "(":
                if cur:
                    stack.append(cur)
            elif token == ")":
                if stack:
                    stack.pop()
            else:
                cur = TreeBinary.Node(token)

                if not isRoot:
                    self.root = cur
                    isRoot = True

                if not stack:
                    continue

                parent = stack[-1]

                if not parent.left:
                    parent.left = cur
                else:
                    parent.right = cur


class TreeNodeThreaded:
    def __init__(self, data: str | None = None):
        self.data = data
        self.left: TreeNodeThreaded | None = None
        self.right: TreeNodeThreaded | None = None
        self.right_thread = self.left_thread = False
    
    def __repr__(self) -> str:
        return f"{self.data!r}"


class TreeBinaryThreadedBuilder:
    @staticmethod
    def build(root: TreeNodeThreaded | None) -> TreeNodeThreaded:
        head = TreeNodeThreaded()
        head.left, head.right = root, head
        head.left_thread = False
        head.right_thread = True

        def thread_nodes(node: TreeNodeThreaded | None, prev: list[TreeNodeThreaded]):
            if node is None:
                return

            if not node.left_thread:
                thread_nodes(node.left, prev)

            if prev[0]:
                if prev[0].right is None:
                    prev[0].right = node
                    prev[0].right_thread = True
                if node.left is None:
                    node.left = prev[0]
                    node.left_thread = True

            prev[0] = node

            if not node.right_thread:
                thread_nodes(node.right, prev)

        prev = [head]
        thread_nodes(root, prev)

        prev[0].right = head
        prev[0].right_thread = True
        head.right = prev[0]

        return head

    @staticmethod
    def inorder_recursive(root: TreeNodeThreaded | None) -> None:
        def traverse(node: TreeNodeThreaded | None):
            if node is None:
                return
            if not node.left_thread:
                traverse(node.left)
            print(node.data, end=' ')
            if not node.right_thread:
                traverse(node.right)

        traverse(root)


class TreeBinaryThreaded:
    def __init__(self, head: TreeNodeThreaded) -> None:
        self.head = head
    
    def find_successor(self, root: TreeNodeThreaded) -> TreeNodeThreaded | None:
        if root.right_thread:
            return root.right
        node = root.right
        while node and not node.left_thread:
            node = node.left
        return node
    
    def traverse_inorder(self) -> list[TreeNodeThreaded]:
        ret = []
        node = self.head.left
        if node is None:
            return ret

        while not node.left_thread:
            node = node.left

        while node != self.head:
            ret.append(node)
            node = self.find_successor(node)

        return ret


def n_to_tn(node: Optional[TreeBinary.Node]) -> Optional[TreeNodeThreaded]:
    if node is None:
        return None
    new_node = TreeNodeThreaded(node.data)
    new_node.left = n_to_tn(node.left)
    new_node.right = n_to_tn(node.right)
    return new_node


if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )"
    tree_binary = TreeBinary()
    tree_binary.build(sexpr.split())

    threaded_root = n_to_tn(tree_binary.root)
    
    head = TreeBinaryThreadedBuilder.build(threaded_root)
    tree = TreeBinaryThreaded(head)

    actions = tree.traverse_inorder()
    print([node.data for node in actions])
