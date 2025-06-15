class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key)


class TreeBinarySearch:

    def __init__(self):
        self.root = None

    def insert(self, target: int):

        def go(now):

            if not now:
                return Node(target)

            if now.key < target:
                now.right = go(now.right)
            else:
                now.left = go(now.left)

            return now

        if not self.root:
            self.root = Node(target)
            return

        go(self.root)

    def traverse(self) -> list[int]:

        actions = []

        def go(now):

            if not now:
                return

            go(now.left)
            actions.append(now)
            go(now.right)

        go(self.root)
        return actions

    def delete(self, delete_target):

        def go(root, target):
            if root.key < target:
                root.right = go(root.right, target)
            elif root.key > target:
                root.left = go(root.left, target)
            else:
                if not root:
                    return None
                elif not root.left or not root.right:
                    return root.right if root.right else root.left
                else:
                    now = root

                    now = now.left

                    while now.right:
                        now = now.right

                    root.key = now.key

                    root.left = go(root.left, now.key)

            return root

        go(self.root, delete_target)


if __name__ == "__main__":
    tree = TreeBinarySearch()
    elems = [40, 20, 60, 10, 30, 50, 70, 45, 55, 52]
    for i in elems:
        tree.insert(i)

    print(tree.traverse())

    tree.delete(60)
    print(tree.traverse())

    tree.delete(40)
    print(tree.traverse())
