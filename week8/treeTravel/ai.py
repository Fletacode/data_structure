import sys
from typing import List, Optional, Iterator

# Python 3.9+ allows str | None, older versions need Optional[str] or Union[str, None]
# Using Optional for broader compatibility
class TreeBinary:
    class Node:
        def __init__(self, data: Optional[str] = None):
            self.data = data
            self.left: Optional["TreeBinary.Node"] = None
            self.right: Optional["TreeBinary.Node"] = None

        # Use __repr__ for the desired quoted output in print_tree
        def __repr__(self) -> str:
            # return f"'{self.data}'" if self.data is not None else "None"
            # Using !r automatically adds quotes for strings
            return f"{self.data!r}" if self.data is not None else "None"

    def __init__(self) -> None:
        self.root: Optional[TreeBinary.Node] = None

    # Using a recursive build method which is often simpler for S-expressions
    def build(self, sexpr: List[str]) -> None:
        if not sexpr:
            self.root = None
            return

        it = iter(sexpr)
        try:
            self.root = self._build_recursive(it)
            # Check for extra tokens after the main expression
            if next(it, None) is not None:
                 print("Warning: Extra tokens found after main S-expression", file=sys.stderr)
                 # Or raise ValueError("Extra tokens found after main S-expression")
        except (ValueError, StopIteration) as e:
            print(f"Error building tree: {e}", file=sys.stderr)
            self.root = None # Ensure tree is None on error

    def _build_recursive(self, token_iter: Iterator[str]) -> Optional[Node]:
        token = next(token_iter, None)

        if token is None:
            raise ValueError("Unexpected end of S-expression")

        if token == ')': # Should not encounter ')' here in a valid expression part
             raise ValueError("Invalid S-expression: Unexpected ')'")

        if token == '(':
            # Format: ( data left_subtree right_subtree )
            data = next(token_iter, None)
            if data is None or data in ('(', ')'): # Basic validation for data
                raise ValueError(f"Invalid S-expression: Expected data after '(', found '{data}'")

            node = TreeBinary.Node(data)

            # Recursively build left and right children
            node.left = self._build_recursive(token_iter)
            node.right = self._build_recursive(token_iter)

            # Consume the closing parenthesis for the current subtree
            closing_paren = next(token_iter, None)
            if closing_paren != ')':
                raise ValueError(f"Invalid S-expression: Expected ')', found '{closing_paren}'")

            return node
        else:
            # Token is data for a leaf node (e.g., 'A', 'B')
            # No need to check for '#' as per the example S-expression
            return TreeBinary.Node(token)


def print_tree(tree: Optional[TreeBinary]) -> None:
    # 재귀 호출을 위한 내부 헬퍼 함수 정의
    def _print_recursive(node: Optional[TreeBinary.Node], tag="", root=True, left=True) -> None:
        # 노드가 없으면 종료
        if not node:
            return

        # 루트 노드 또는 자식 노드 형식에 맞게 출력 (__repr__ 사용)
        print(f"{node!r}" if root else f"{tag}{'├── ' if left else '└── '}{node!r}")

        # 왼쪽, 오른쪽 자식 노드 존재 여부 확인
        has_left = node.left is not None
        has_right = node.right is not None

        # 자식 노드가 없으면 현재 노드에서 재귀 종료
        if not has_left and not has_right:
            return

        # 다음 레벨의 들여쓰기 및 연결선 계산
        new_tag = "" if root else f"{tag}{'│   ' if left else '    '}"

        # 왼쪽 자식 처리 (실제 자식 노드 전달)
        if has_left:
            _print_recursive(node.left, new_tag, False, True)
        elif has_right: # 왼쪽 없고 오른쪽만 있을 때, 왼쪽 자리에 빈 줄 표시 안함
            pass

        # 오른쪽 자식 처리 (실제 자식 노드 전달)
        if has_right:
            _print_recursive(node.right, new_tag, False, False)
        elif has_left: # 오른쪽 없고 왼쪽만 있을 때, 오른쪽 자리에 빈 줄 표시 안함
            pass

    # --- 외부 함수의 실행 로지크 ---
    if not tree or not tree.root:
        print("Tree is empty.")
        return

    # 내부 재귀 함수 호출 시작
    _print_recursive(tree.root)

# Function to perform inorder traversal iteratively using a stack
def traverse(tree: Optional[TreeBinary]) -> List[Optional[str]]:
    result_list: List[Optional[str]] = []
    stack: List[TreeBinary.Node] = [] # Initialize an empty list as the stack
    current: Optional[TreeBinary.Node] = tree.root if tree else None # Start from the root

    # Loop while there's a node to process or the stack is not empty
    while current is not None or stack:
        # 1. Reach the leftmost node of the current node
        while current is not None:
            stack.append(current) # Push the node onto the stack before going left
            current = current.left

        # 2. Current must be None at this point. Pop the last node added.
        # This node is the next one to be visited in inorder sequence.
        current = stack.pop()
        result_list.append(current.data) # Visit the node (add its data)

        # 3. Now, traverse the right subtree
        current = current.right # Move to the right child

    return result_list

if __name__ == "__main__":
    tree = TreeBinary()
    # Ensure correct spacing for split()
    sexpr_str = "( + ( * ( * ( / A B ) C ) D ) E )"
    tokens = sexpr_str.replace('(', ' ( ').replace(')', ' ) ').split()
    tokens = [token for token in tokens if token] # Remove empty strings if any

    print("Building tree...")
    tree.build(tokens)

    print("\nTree structure:")
    print_tree(tree)

    print("\nInorder traversal (Iterative):")
    actions = traverse(tree)
    # Format the output list like ['A', '/', 'B', '*', 'C', '*', 'D', '+', 'E']
    print([item for item in actions]) # Simple list print
    # Or print(f"{actions!r}") for exact ['A', ..., 'E'] format