from typing import List, Optional
try:
    from typing import LiteralString
except ImportError:
    try:
        from typing_extensions import LiteralString
    except ImportError:
        LiteralString = str
import sys

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
def print_tree(tree: Optional[TreeBinary]) -> None:
    def _print_recursive(node: Optional[TreeBinary.Node], tag="", root=True, left=True) -> None:
        if not node:
            return

        print(f"{node.data}" if root else f"{tag}{'├── ' if left else '└── '}{node.data}")

        has_left = node.left is not None
        has_right = node.right is not None

        if not has_left and not has_right:
            return

        new_tag = "" if root else f"{tag}{'│   ' if left else '    '}"

        if has_left:
            _print_recursive(node.left, new_tag, False, True)
        elif has_right:
             pass

        if has_right:
            _print_recursive(node.right, new_tag, False, False)
        elif has_left:
             pass

    if not tree or not tree.root:
        print("Tree is empty.")
        return

    _print_recursive(tree.root)


if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( 30 ( 5 ( # 2 ) 40 ( 80 # ) ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( D ( H I ) E ) C ( F G ) ) ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( # D ) # ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( C ( D ( E # ) # ) # ) # ) )".split())
    print_tree(tree)