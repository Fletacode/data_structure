import sys
from typing import List, Optional, Iterator
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

        def __repr__(self) -> str:
            return str(self.data) if self.data is not None else "None"

    def __init__(self) -> None:
        self.root: Optional[TreeBinary.Node] = None

    def build(self, sexpr: List[LiteralString]) -> None:
        if not sexpr:
            self.root = None
            return

        it = iter(sexpr)
        try:
            self.root = self._build_recursive(it)
            if next(it, None) is not None:
                raise ValueError("Extra tokens found after main S-expression")
        except (ValueError, StopIteration) as e:
            print(f"Error building tree: {e}", file=sys.stderr)
            self.root = None

    def _build_recursive(self, token_iter: Iterator[LiteralString]) -> Optional[Node]:
        token = next(token_iter, None)

        if token is None:
            raise ValueError("Unexpected end of S-expression")

        if token == '#':
            return TreeBinary.Node('#')

        if token == '(':
            data = next(token_iter, None)
            if data is None or data in ('(', ')', '#'):
                raise ValueError(f"Invalid S-expression: Expected data after '(', found '{data}'")

            node = TreeBinary.Node(data)
            node.left = self._build_recursive(token_iter)
            node.right = self._build_recursive(token_iter)

            closing_paren = next(token_iter, None)
            if closing_paren != ')':
                raise ValueError(f"Invalid S-expression: Expected ')', found '{closing_paren}'")

            return node
        elif token == ')':
             raise ValueError("Invalid S-expression: Unexpected ')'")
        else:
            # Token is data for a leaf node
            return TreeBinary.Node(token)

    @staticmethod
    def _print_recursive_helper(node: Optional["TreeBinary.Node"], prefix: str, is_left: bool, is_root: bool):
        if node is None:
            return

        if is_root:
            print(node.data)
            current_prefix_for_children = ""
        else:
            connector = "├── " if is_left else "└── "
            print(f"{prefix}{connector}{node.data}")
            current_prefix_for_children = prefix + ("│   " if is_left else "    ")

        left_child = node.left
        right_child = node.right

        if left_child:
            TreeBinary._print_recursive_helper(left_child, current_prefix_for_children, True, False)

        if right_child:
            TreeBinary._print_recursive_helper(right_child, current_prefix_for_children, False, False)

def print_tree(tree: Optional[TreeBinary]) -> None:
    if not tree or not tree.root:
        return
    TreeBinary._print_recursive_helper(tree.root, "", True, True)



if __name__ == "__main__":
    sexprs = [
        "( 30 ( 5 # 2 ) ( 40 80 # ) )",
        "( A ( B ( D H I ) E ) ( C F G ) )",
        "( A ( B # D ) # )",
        "( A ( B ( C ( D E # ) # ) # ) # )",
    ]

    for i, sexpr_str in enumerate(sexprs):
        print(f"--- Tree {i+1} ---")
        tree = TreeBinary()
        tokens_with_spaces = sexpr_str.replace('(', ' ( ').replace(')', ' ) ')
        tokens = tokens_with_spaces.split()
        tokens = [token for token in tokens if token]
        tree.build(tokens)
        print_tree(tree)
        print("-" * 15)
