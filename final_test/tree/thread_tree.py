# 쓰레드 트리 inorder 재귀,스택 사용하지 않고도 자료구조적으로 해결 (임베디드 시스템에 활용)
# TreeBinary -> ThreadTree 로 변경


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


class NodeThread:

    def __init__(self, data=None):
        self.data = data
        self.left, self.right = None, None
        self.left_thread, self.right_thread = False, False

    def __repr__(self):
        return str(self.data)


class TreeBinaryThread:
    def __init__(self):
        self.root = None
        self.head = None

    def changeToThread(self, root: Node) -> NodeThread:

        def go(node):

            node_thread = NodeThread(node.data)

            if node.left:
                node_thread.left = go(node.left)
            if node.right:
                node_thread.right = go(node.right)

            return node_thread

        self.root = go(root)
        return self.root

    def build(self):
        self.head = NodeThread()
        self.head.right = self.head
        self.head.left = self.root

        prev = self.head

        def go(now):
            nonlocal prev

            if now.left:
                go(now.left)

            if prev:
                if not now.left:
                    now.left_thread = True
                    now.left = prev
                if not prev.right:
                    prev.right_thread = True
                    prev.right = now

            prev = now

            if now.right:
                go(now.right)

        go(self.root)
        prev.right = self.head
        prev.right_thread = True

    def find_successor(self, now: NodeThread):

        if now.right_thread:
            return now.right

        now = now.right

        while not now.left_thread:
            now = now.left

        return now

    def traverse_inorder(self) -> list[NodeThread]:

        actions = []

        now = self.head.left

        while not now.left_thread:
            now = now.left

        while now != self.head:
            actions.append(now)
            now = self.find_successor(now)

        return actions

    def search(self, target: int):

        # 재귀로 구현
        # def go(now):
        #     if now.data == target:
        #         return now

        #     node = None

        #     if not now.left_thread:
        #         node = go(now.left)
        #     if not now.right_thread:
        #         node = go(now.right)

        #     return node

        # return go(self.root)

        # thread 사용

        now = self.head.left

        while not now.left_thread:
            now = now.left

        while now != self.head:
            if now.data == target:
                return now
            now = self.find_successor(now)

        return None

    def insert(self, dst: int, src):

        new_node = NodeThread(src)

        find_node = self.search(dst)

        new_node.right_thread = find_node.right_thread
        find_node.right_thread = False

        new_node.right = find_node.right
        find_node.right = new_node

        new_node.left_thread = True
        new_node.left = find_node


if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )"
    tree_binary = TreeBinary()
    tree_binary.build(sexpr.split())
    tree_thread = TreeBinaryThread()
    tree_thread.changeToThread(tree_binary.root)
    tree_thread.build()

    print(tree_thread.traverse_inorder())
    print(tree_thread.search("C"))
    print(tree_thread.search("Z"))

    tree_thread.insert(dst="E", src="Z")
    print(tree_thread.traverse_inorder())

    tree_thread.insert(dst="C", src="Y")
    print(tree_thread.traverse_inorder())
