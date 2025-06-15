from typing import Optional, List
from typing import List, Optional
try:
    from typing import LiteralString
except ImportError:
    try:
        from typing_extensions import LiteralString
    except ImportError:
        LiteralString = str
import sys


class TreeNodeThreaded:
    def __init__(self, data: str | None = None):
        self.data = data
        self.left: TreeNodeThreaded | None = None
        self.right: TreeNodeThreaded | None = None
        self.right_thread = self.left_thread = False
    def __repr__(self) -> str:
        return f"{self.data}" 

class TreeBinaryThreaded:
    def __init__(self, data: TreeNodeThreaded):
        self.head = data

    def find_successor(self, root: TreeNodeThreaded = None) -> TreeNodeThreaded | None:
        
        if root.right_thread:
            return root.right

        root = root.right

        while not root.left_thread:
            root = root.left
        return root


    def traverse_inorder(self) -> list[TreeNodeThreaded]:
        ret = []

        now = self.head

        while not now.left_thread:
            now = now.left
        
        while now != self.head:
            ret.append(now.data)
            now = self.find_successor(now)

        return ret
    
    def search(self, data):

        ret = []

        now = self.head

        if now.data == data:
            return now

        while not now.left_thread:
            now = now.left
            if now.data == data:
                return now
        
        while now != self.head:
            ret.append(now.data)
            now = self.find_successor(now)
            if now.data == data:
                return now

    def insert(self, dst, src):
        find_node = self.search(dst)
        new_node = TreeNodeThreaded(src)

        temp = find_node.right
        find_node.right = new_node
        new_node.right = temp
        new_node.right_thread = True
        new_node.left = find_node
        new_node.left_thread = True

class TreeBinaryThreadedBuilder:
   
    def build(root: TreeNodeThreaded | None) -> TreeNodeThreaded:
        head = TreeNodeThreaded()
        head.left, head.right = root, head
        head.left_thread = False
        head.right_thread = False

        prev = head

        def go(now):
            nonlocal prev

            if now is None:
                return

            if now.left is not None:
                go(now.left)

            if prev:
                if prev.right is None:
                    prev.right_thread = True
                    prev.right = now
                if now.left is None:
                    now.left_thread = True
                    now.left = prev

            prev = now

            if now.right is not None:
                go(now.right)
        
        
        go(root)
        prev.right = head
        prev.right_thread = True

        return head


    @staticmethod
    def inorder_recursive(root: TreeNodeThreaded | None) -> None:
        

        if not root.left_thread:
            TreeBinaryThreadedBuilder.inorder_recursive(root.left)        
        print(root.data, end="")
        if not root.right_thread:
            TreeBinaryThreadedBuilder.inorder_recursive(root.right)
    
    @staticmethod
    def change_to_ThreadNode(root):
        
        if root is None:
            return None

        new_node = TreeNodeThreaded(root.data)
        if root.left is not None:
            new_node.left = TreeBinaryThreadedBuilder.change_to_ThreadNode(root.left)
        if root.right is not None:
            new_node.right = TreeBinaryThreadedBuilder.change_to_ThreadNode(root.right) 


        return new_node

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
        i = 0
        stack : List[TreeBinary.Node] = []
        root:Optional[TreeBinary.Node] = None

        while i < len(sexpr):
            token = sexpr[i]
            if token == '(':
                pass
            elif token == ')':
                if stack:
                    stack.pop()
            else:
                node = TreeBinary.Node(token)
                if not stack:
                    root = node
                else:
                    parent = stack[-1]
                    if parent.left is None:
                        parent.left = node
                    else:
                        parent.right = node

                if i+1 < len(sexpr) and sexpr[i+1] == '(':
                    stack.append(node)
            i += 1

        self.root = root

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )"
    
    # sexpr = "( A ( B C ) )".split()
    # sexpr = "( A )".split()
    tree_binary = TreeBinary()
    tree_binary.build(sexpr.split())
    new_root = TreeBinaryThreadedBuilder.change_to_ThreadNode(tree_binary.root)
    head = TreeBinaryThreadedBuilder.build(new_root)
    # TreeBinaryThreadedBuilder.inorder_recursive(new_root)
    tree = TreeBinaryThreaded(head)
    actions = tree.traverse_inorder()
    print(actions)

    node = tree.search('A')
    print(node)
    tree.insert('E','Z')

    actions = tree.traverse_inorder()
    print(actions)

    tree.insert('C','Y')
    actions = tree.traverse_inorder()
    print(actions)
    
    