# csr
# 2026/1/11 下午8:13
# 2
class TreeNode:
    def __init__(self, w):
        self.w = w
        self.left = None
        self.right = None


class BiTree:
    def __init__(self):
        self.root = None
        self.q = []

    def add_node(self, w):
        x = TreeNode(w)
        if self.root is None:
            self.root = x
            self.q.append(x)
        else:
            if self.q[0].left is None:
                self.q[0].left = x
            else:
                self.q[0].right = x
                self.q.pop(0)
        self.q.append(self)

    def level_order(self):
        q = [self.root]
        while q:
            x = q.pop(0)
            print(x.w, end=" ")
            if x.left is not None:
                q.append(x.left)
            if x.right is not None:
                q.append(x.right)

    def pre_order(self, root):
        if root is None:
            return
        print(root.w, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.w, end=" ")
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.w, end=" ")


if __name__ == '__main__':
    t = BiTree()
    t.add_node(1)
    t.add_node(2)
    t.add_node(3)
    t.level_order()
    print('')
    t.pre_order(t.root)
    print('')
    t.in_order(t.root)
    print('')
    t.post_order(t.root)
