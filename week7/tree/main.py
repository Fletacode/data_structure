from typing import List, Optional, TypeVar, Union

LiteralString = str

class Tree:
    class Node:
        def __init__(self, data: str) -> None:
            self.data = data
            self.left_child: Optional[Tree.Node] = None
            self.right_sibling: Optional[Tree.Node] = None
        
        def __repr__(self) -> str:
            return f"{self.data}"

    def __init__(self) -> None:
        self.root: Optional[Tree.Node] = None

    def build(self, sexpr: List[LiteralString]) -> Optional["Tree.Node"]:
        stack: List[Tree.Node] = []
        root: Optional[Tree.Node] = None
        i = 0
        
        while i < len(sexpr):
            token = sexpr[i]
            
            if token == "(":
                i += 1
                continue
            elif token == ")":
                if stack:
                    stack.pop()
            else:
                node = Tree.Node(token)
                
                if not stack:  
                    root = node
                else:  
                    parent = stack[-1]
                    if parent.left_child is None:  
                        parent.left_child = node
                    else:  
                        sibling = parent.left_child
                        while sibling.right_sibling:
                            sibling = sibling.right_sibling
                        sibling.right_sibling = node
                
              
                if i + 1 < len(sexpr) and sexpr[i + 1] == "(":
                    stack.append(node)
            
            i += 1
        
        self.root = root
        return root

def display_tree(tree: Tree) -> None:
    """iterative using stack"""
    def print_tree_iterative(root: Optional[Tree.Node]) -> None:
        if root is None:
            return
     
        stack = [(root, 0, True, "")]
        visited = set()
        
        print(root.data)
        
       
        def push_children(node: Tree.Node, depth: int, prefix: str) -> None:
            child = node.left_child
            children = []
            
         
            while child:
                children.append(child)
                child = child.right_sibling
            
           
            for i in range(len(children) - 1, -1, -1):
                is_last = (i == len(children) - 1)
                new_prefix = prefix
                
                if depth > 0:
                    new_prefix += " " if prefix.endswith("└──") else "│ "
                
                stack.append((children[i], depth + 1, is_last, new_prefix))
        
       
        def node_id(node, depth):
            return f"{id(node)}_{depth}"
        
        while stack:
            node, depth, is_last, prefix = stack.pop()
            
           
            nid = node_id(node, depth)
            if nid in visited:
                continue
            visited.add(nid)
            

            if depth > 0:
                print(f"{prefix}{'└──' if is_last else '├──'} {node}")
            
            push_children(node, depth, prefix)
    
    print_tree_iterative(tree.root)

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
        
        
        child = node.left_child
        
       
        children = []
        while child:
            children.append(child)
            child = child.right_sibling
        
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
    display_tree(tree)  
