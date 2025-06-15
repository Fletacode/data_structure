# simple_tree와 다르게 양쪽 둘다 연결


class Node:
    def __init__(self, data):
        self.data = data
        self.left: None | Node = None
        self.right: None | Node = None

    def __repr__(self):
        return str(self.data)


class TreeBinary:

    def __init__(self):
        self.root: Node | None = None

    def build(self, sexpr):

        stack = []
        root = None
        for idx, token in enumerate(sexpr):
            if token == "(":
                continue
            elif token == ")":
                if len(stack) > 0:
                    stack.pop()
            else:
                new_node = Node(token)
                if not stack:
                    root = new_node
                else:
                    now = stack[-1]

                    if now.left is None:
                        now.left = new_node
                    elif now.right is None:
                        now.right = new_node

                if idx + 1 < len(sexpr) and sexpr[idx + 1] == "(":
                    stack.append(new_node)

        self.root = root
        return root


def print_tree(root: Node):

    def go(root, isLast=True, isRoot=True, tag=""):

        if isRoot:
            print(root)
        else:
            print(f"{tag}{"|_" if isLast else "|-"}{root}")

        if root.left:
            last = True if root.right is None else False
            new_tag = tag
            new_tag += " " if isLast else "| "
            new_tag = "" if isRoot else new_tag
            go(root.left, last, False, new_tag)

        if root.right:
            new_tag = tag
            new_tag += " " if isLast else "| "
            new_tag = "" if isRoot else new_tag
            go(root.right, True, False, new_tag)

    go(root)


if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( 30 ( 5 ( # 2 ) 40 ( 80 # ) ) )".split())
    print_tree(tree.root)

    tree.build("( A ( B ( D ( H I ) E ) C ( F G ) ) ) )".split())
    print_tree(tree.root)

    tree.build("( A ( B ( # D ) # ) )".split())
    print_tree(tree.root)
    tree.build("( A ( B ( C ( D ( E # ) # ) # ) # ) )".split())
    print_tree(tree.root)
