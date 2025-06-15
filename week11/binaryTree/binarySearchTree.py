class TreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    def __repr__(self) -> str:
        return f"{self.key}"
    
class TreeBinarySearch:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

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

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        now = self.root

        while now is not None:
            if now.key > data:
                if now.left is None:
                    now.left = TreeNode(data)
                    return
                now = now.left
            elif now.key < data:
                if now.right is None:
                    now.right = TreeNode(data)
                    return
                now = now.right
            else:
                return
            
    def delete(self, data):
        
        def delete_recursive(now , key):

            if now is None:
                return None

            if now.key < key:
                now.right = delete_recursive(now.right,key)
            elif now.key > key:
                now.left = delete_recursive(now.left,key)
            else:

                if now.left is None or now.right is None:
                    now = now.right if now.left is None else now.left
                    return now
                else:   
                    node = now.left

                    while node.right is not None:
                        node = node.right

                    now.key = node.key
                    now.left = delete_recursive(now.left,node.key)
                
            return now
            
        
        self.root = delete_recursive(self.root, data)
    
if __name__ == "__main__":
    tree = TreeBinarySearch()
    elems = [40, 20, 60, 10, 30, 50, 70, 45, 55, 52]
    for i in elems:
        tree.insert(i)

    actions = tree.traverse()
    print(actions)

    tree.delete(60)

    actions = tree.traverse()
    print(actions)
