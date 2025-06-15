class TreeNode:
    def __init__(self, key: int | str) -> None:
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    
    def __repr__(self) -> str:
        return f"{self.key}"


class TreeBinaryBuilder:
    @staticmethod
    def build(sexpr: list[int | str]) -> TreeNode | None:
        stack: list[TreeNode] = []
        add = lambda node: node if node.key != "#" else None
        root = None

        for token in sexpr:
            if token != ")":
                stack.append(TreeNode(token))
                continue

            root_ = None
            while stack[-1].key != "(":
                node = stack.pop()
                if not root_:
                    root_ = node
                    continue

                right, root_ = root_, TreeNode("")
                root_.left, root_.right = add(node), add(right)

            stack.pop()
            if not stack:
                return root_
            assert root_
            root = stack.pop()
            root_.key = root.key
            stack.append(root_)

        return root
    
class TreeBinarySearch:

    def __init__(self, root: TreeNode | None = None) -> None:
        self.root = root

    def search_iter(self,key):
        
        now = self.root

        while now is not None:
            if now.key < key:
                now = now.right
            elif now.key > key:
                now = now.left
            elif now.key == key:
                return now.key
            else:
                return None

        

    def search(self, key: int) -> TreeNode | None:
        """using recursive fashion"""

        def search_recursive(now: TreeNode | None, key) -> TreeNode | None:
            
            if now is None:
                return None

            if now.key == key:
                return now
            
            if now.key > key:
                return search_recursive(now.left, key)
            else:
                return search_recursive(now.right, key)

        return search_recursive(self.root, key)
    
   


if __name__ == "__main__":
    sexpr = "( 44 ( 17 ( # 32 ( 28 ( # 29 ) # ) ) 88 ( 65 ( 54 82 ( 76 ( #80 ) # ) ) 97 ) ) )".split()
    print(sexpr)
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = TreeBinaryBuilder.build(sexpr)

    print(root.key)

    bst = TreeBinarySearch(root)
    print(bst.search(17).key)

    print(bst.search_iter(32))