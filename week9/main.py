class TreeNode:
    def __init__(self, data: str | None = None):
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    def __repr__(self) -> str:
        return f"{self.data!r}"

class TreeBinary:
    def __init__(self):
        self.root: TreeNode | None = None

    def build(self, sexpr: list[str]):
        if not sexpr:
            self.root = None
            return
            
        stack = []
        it = iter(sexpr)
        root = None
        try:
            while True:
                token = next(it)
                if token == ')':
                    
                    node = stack.pop()
                    if stack:
                        parent = stack[-1]
                        if parent.left is None:
                            parent.left = node
                        else:
                            parent.right = node
                    else:
                        
                        root = node
                elif token == '(':
                    
                    data = next(it)
                    new_node = TreeNode(data)
                    stack.append(new_node)
                
        except StopIteration:
            pass
        self.root = root

class TreeNodeThreaded:
    def __init__(self, data: str | None = None):
        self.data = data
        self.left: TreeNodeThreaded | None = None
        self.right: TreeNodeThreaded | None = None
        
        self.right_thread = self.left_thread = False

    def __repr__(self) -> str:
        return f"{self.data!r}"


class TreeBinaryThreadedBuilder:
    
    prev: TreeNodeThreaded | None = None

    @staticmethod
    def build(root: TreeNode | None) -> TreeNodeThreaded:
        """표준 이진 트리를 스레드 이진 트리로 변환하고 헤드 노드를 반환합니다."""
        
        head = TreeNodeThreaded()
        head.left = root  
        head.right = head 
        head.right_thread = True 
        head.left_thread = False 

        
        TreeBinaryThreadedBuilder.prev = head

        threaded_root = TreeBinaryThreadedBuilder._convert_and_thread(root, head)

        head.left = threaded_root if threaded_root else head 

        if TreeBinaryThreadedBuilder.prev:
             TreeBinaryThreadedBuilder.prev.right = head
             TreeBinaryThreadedBuilder.prev.right_thread = True
             
        
        
        
        TreeBinaryThreadedBuilder.prev = None

        return head 

    @staticmethod
    def _convert_and_thread(node: TreeNode | None, head: TreeNodeThreaded) -> TreeNodeThreaded | None:
        """재귀적으로 노드를 변환하고 스레드를 설정합니다."""
        if node is None:
            return None

        threaded_node = TreeNodeThreaded(node.data)
        threaded_node.left = TreeBinaryThreadedBuilder._convert_and_thread(node.left, head)

        if TreeBinaryThreadedBuilder.prev and not TreeBinaryThreadedBuilder.prev.right_thread and TreeBinaryThreadedBuilder.prev.right is None:
             TreeBinaryThreadedBuilder.prev.right = threaded_node
             TreeBinaryThreadedBuilder.prev.right_thread = True
             
        
        if threaded_node.left is None:
            threaded_node.left = TreeBinaryThreadedBuilder.prev
            threaded_node.left_thread = True

        
        TreeBinaryThreadedBuilder.prev = threaded_node

        
        threaded_node.right = TreeBinaryThreadedBuilder._convert_and_thread(node.right, head)
        

        return threaded_node


class TreeBinaryThreaded:
    def __init__(self, head: TreeNodeThreaded):
        
        self.head: TreeNodeThreaded = head

    def find_successor(self, node: TreeNodeThreaded) -> TreeNodeThreaded | None:
        """스레드 이진 트리에서 주어진 노드의 중위 후속자를 찾습니다."""
        
        if node.right_thread:
            
            return node.right if node.right != self.head else None 
        
        else:
            current = node.right
            if current is None: 
                 return None
            
            while current and not current.left_thread:
                 current = current.left
            return current

    def traverse_inorder(self) -> list[str]:
        """스레드를 사용하여 중위 순회를 수행하고 노드 데이터 리스트를 반환합니다."""
        result: list[str] = []
        
        current = self.head.left 

        if current is None or current == self.head: 
            return result
            
        
        while current and not current.left_thread:
             
            if current.left is None:
                 break
            current = current.left

        
        while current is not None and current != self.head:
            
            if current.data:
                result.append(current.data)

            
            current = self.find_successor(current)
            
            
            if len(result) > 1000: 
                 print("Warning: Traversal limit exceeded, potential loop.")
                 break

        return result

if __name__ == "__main__":
    
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
        
    tree_binary = TreeBinary()
    tree_binary.build(sexpr)
    head_node = TreeBinaryThreadedBuilder.build(tree_binary.root)
    # threaded_tree = TreeBinaryThreaded(head_node)
    # actions = threaded_tree.traverse_inorder()

    
    # print(actions) 

    
