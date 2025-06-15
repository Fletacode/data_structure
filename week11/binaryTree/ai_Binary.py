class TreeNode:
    def __init__(self, key: int | str) -> None:
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    
    def __repr__(self) -> str:
        return f"{self.key!r}"


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


    def traverse(self) -> list[TreeNode]:
        if not self.root:
            return []
        
        ret: list[TreeNode] = []
        stack: list[TreeNode] = []
        root = self.root
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root)
            root = root.right
        
        return ret
    
    
    def search(self, key: int) -> TreeNode | None:
        cur = self.root

        while cur:
            if key == cur.key:
                break

            if key < cur.key: cur = cur.left
            else: cur = cur.right

        return cur       

    def insert(self, key: int) -> None:
        """using iterative fashion"""
        if not self.root:
            self.root = TreeNode(key)
            return
        
        cur = self.root

        while cur:
            if key == cur.key:
                return

            if key < cur.key:
                if cur.left: cur = cur.left
                else:        cur.left = TreeNode(key)
            else: 
                if cur.right: cur = cur.right
                else:         cur.right = TreeNode(key)

    def delete(self, key: int) -> None:
        """using recursive fashion"""

        def delete_recursive(root: TreeNode | None, key: int) ->TreeNode | None:
            """inner function"""
            if key == root.key:
                if not root.left and not root.right:
                    root = None
                elif root.left is None or root.right is None:
                    root = root.left if root.right is None else root.right
                else: 
                    subtree = root.left
                    while subtree.right:
                        subtree = subtree.right
                    root.key = subtree.key
                    root.left = delete_recursive(root.left, subtree.key)
                
                return root

            if key < root.key:
                root.left = delete_recursive(root.left, key)
            elif key > root.key:
                root.right = delete_recursive(root.right, key)
            
            return root
        
        self.root = delete_recursive(self.root, key)
    
if __name__ == "__main__":
    tree = TreeBinarySearch()
    elems = [40, 20, 60, 10, 30, 50, 70, 45, 55, 52]
    for i in elems:
        tree.insert(i)
    actions = tree.traverse()
    print(actions)
    
    n = 60
    print(f"node_deleted = {n}")
    tree.delete(n)
    actions = tree.traverse()
    print(actions)
    
    # n = 40
    # print(f"node_deleted = {n}")
    # tree.delete(n)
    # actions = tree.traverse()
    # print(actions)

