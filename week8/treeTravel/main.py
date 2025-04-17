from typing import Optional,List

class TreeBinary:
    class Node:
        def __init__(self, data: Optional[str] = None):
            self.data = data
            self.left: Optional["TreeBinary.Node"] = None
            self.right: Optional["TreeBinary.Node"] = None

        def __repr__(self):
            return f"{self.data}"


    def build(self, sexpr: List[str]) -> None:
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


def traverse(tree: TreeBinary = None) -> List[TreeBinary.Node]:
    if not tree:
        return []
    ret: list[TreeBinary.Node] = []
    stack: list[TreeBinary.Node] = []
    root: TreeBinary.Node | None = tree.root


    now = root
    while now is not None or stack:

        while now is not None:
            stack.append(now)
            now = now.left

        now = stack.pop()
        ret.append(now)

        now = now.right

    return ret


if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( + ( * ( * ( / ( A B ) C ) D ) E ) )".split())
    print_tree(tree)

    actions = traverse(tree)

    print(actions)
