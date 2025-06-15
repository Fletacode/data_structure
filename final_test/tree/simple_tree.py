# 왼쪽에다가 자식들 몰빵 부모 노드에 오른쪽 자식 없음 왼쪽꺼 하나로 연결해서 쭉 연결ㄴ
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right_sibling = None

    def __repr__(self):
        return str(self.data)


class Tree:

    def __init__(self):
        self.root = None

    def build(self, sexpr):

        stack = []
        idx = 0
        self.root = None
        while idx < len(sexpr):
            token = sexpr[idx]

            if token == "(":
                pass
            elif token == ")":
                if len(stack) > 0:
                    stack.pop()
            else:

                new_node = Node(token)

                if not stack:
                    root = new_node
                else:
                    now = stack[-1]
                    if not now.left:
                        now.left = new_node
                    else:
                        now = now.left
                        while now.right_sibling:
                            now = now.right_sibling
                        now.right_sibling = new_node

            if idx + 1 < len(sexpr) and sexpr[idx + 1] == "(":
                stack.append(new_node)

            idx += 1

        self.root = root

    def print_tree(self):

        def go(root, isLast=True, isRoot=True, tag=""):

            if isRoot:
                print(root)
            else:
                if not isLast:
                    print(f"{tag}|-{root}")
                else:
                    print(f"{tag}|_{root}")

            children = []
            root = root.left
            while root:
                children.append(root)
                root = root.right_sibling

            for idx, node in enumerate(children):
                last = idx == len(children) - 1
                new_tag = tag

                if not isRoot:
                    new_tag += " " if isLast else "| "
                    # new_tag += "| "

                go(node, last, False, new_tag)

        go(self.root)


if __name__ == "__main__":
    tree = Tree()
    sexpr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    # print(sexpr.split())
    tree.build(sexpr.split())

    tree.print_tree()
    # print(tree.root.data)
