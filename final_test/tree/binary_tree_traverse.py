# 이진트리로 구현, 스택으로 프린트 구현, pre,in,post order 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class TreeBinary:

    def __init__(self):
        self.root = None

    def build(self, sexpr):

        root = None
        stack = []

        for idx, token in enumerate(sexpr):
            if token == "(":
                pass
            elif token == ")":
                if stack:
                    stack.pop()
            else:
                new_node = Node(token)
                if not stack:
                    root = new_node
                else:
                    now = stack[-1]

                    if not now.left:
                        now.left = new_node
                    elif not now.right:
                        now.right = new_node

                if idx + 1 < len(sexpr) and sexpr[idx + 1] == "(":
                    stack.append(new_node)

        self.root = root
        return root


def print_tree(root):

    stack = []
    # isLast, isRoot, tag
    stack.append((root, True, True, ""))

    while stack:
        now, isLast, isRoot, tag = stack.pop()

        if isRoot:
            print(now)
        else:
            print(f"{tag}{"|_" if isLast else "|-"}{now}")

        if now.right:
            new_tag = tag
            new_tag += " " if isLast else "| "
            new_tag = "" if isRoot else new_tag
            stack.append((now.right, True, False, new_tag))

        if now.left:
            last = True if now.right is None else False
            new_tag = tag
            new_tag += " " if isLast else "| "
            new_tag = "" if isRoot else new_tag
            stack.append((now.left, last, False, new_tag))


def traverse_in(tree: TreeBinary):
    root = tree.root
    actions = []

    def go(now):

        if now.left:
            go(now.left)
        actions.append(now)
        if now.right:
            go(now.right)

    go(root)

    return actions


def traverse_in_stack(tree: TreeBinary):

    stack = []
    root = tree.root

    stack.append(root)
    actions = []

    while stack:
        now = stack.pop()

        while now.left:
            stack.append(now)
            next = now.left
            now.left = None
            now = next

        if now.right:
            stack.append(now.right)

        actions.append(now)

    return actions


if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( + ( * ( * ( / ( A B ) C ) D ) E ) )".split())
    print(tree.root)
    print_tree(tree.root)
    actions = traverse_in(tree)
    print(actions)
    print(traverse_in_stack(tree))
