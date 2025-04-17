from typing import Optional, List, LiteralString


class Tree:
    class Node:
        def __init__(self, data: str) -> None:
            self.data = data
            self.left_child: Optional[Tree.Node] = None
            self.right_sibling: Optional[Tree.Node] = None
        def __repr__(self) -> str:
            return f"{self.data}"

    def __init__(self):
        self.root = None

    def build(self, sexpr: List[LiteralString]) -> Optional["Tree.Node"]:
        stack: List[Tree.Node] = []
        root: Tree.Node = None


        i = 0
        while i < len(sexpr):
            if sexpr[i] == '(':
                pass
            elif sexpr[i] == ')':
                if len(stack) > 0:
                    stack.pop()

            else:
                token = sexpr[i]
                node = Tree.Node(token)

                if len(stack) == 0:
                    root = node

                else:
                    parent = stack[-1]
                    if parent.left_child is None:
                        parent.left_child = node
                    else:
                        sibling = parent.left_child
                        while sibling.right_sibling is not None:
                            sibling = sibling.right_sibling
                        sibling.right_sibling = node

                if i+1 < len(sexpr) and sexpr[i+1] == '(':
                    stack.append(node)

            i += 1

        self.root = root

def dislay_tree(tree: Tree) -> None:
    """iterative using stack"""
    pass


def print_tree(tree: Tree) -> None:
    def print_tree_recursive(
            node: Optional[Tree.Node],
            tag: str = "",
            last: bool = True,
            root: bool = True,
    ) -> None:
        if node is None:
            return

        if root:
            print(f"{node}")
        else:
            print(f"{tag}{'└──' if last else '├──'} {node}")

        # 왼쪽 자식 노드를 처리
        child = node.left_child

        # 모든 자식 노드를 리스트로 수집
        children = []
        while child:
            children.append(child)
            child = child.right_sibling

        # 각 자식 노드에 대해 재귀적으로 처리
        for i, child in enumerate(children):
            is_last = (i == len(children) - 1)
            new_tag = tag

            if not root:
                new_tag += ' ' if last else '│ '

            print_tree_recursive(
                child,
                tag=new_tag,
                last=is_last,
                root=False,
            )

    print_tree_recursive(tree.root)

if __name__ == "__main__":
    expr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    tree = Tree()
    tree.build(expr.split())
    print_tree(tree)
    print()
