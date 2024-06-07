class TreeNode:
    """树节点类"""

    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.height = 1


class AVLTree:
    """AVL树类"""

    def __init__(self):
        self._root: TreeNode | None = None

    def height(self, node: TreeNode | None) -> int:
        """获取节点高度"""
        return node.height if node else 0

    def update_height(self, node: TreeNode):
        """更新节点高度"""
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: TreeNode) -> int:
        """获取节点平衡因子"""
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y: TreeNode) -> TreeNode:
        """右旋"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x: TreeNode) -> TreeNode:
        """左旋"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def rotate(self, node: TreeNode) -> TreeNode:
        """旋转操作，使子树重新恢复平衡"""
        balance = self.balance_factor(node)
        # 左左情况
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        # 左右情况
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # 右右情况
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        # 右左情况
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, val: int):
        """插入节点"""
        self._root = self.insert_helper(self._root, val)

    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        """递归插入节点（辅助方法）"""
        if node is None:
            return TreeNode(val)
        # 1. 查找插入位置并插入节点
        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)
        else:
            # 重复节点不插入，直接返回
            return node
        # 更新节点高度
        self.update_height(node)
        # 2. 执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)

    def remove(self, val: int):
        """删除节点"""
        self._root = self.remove_helper(self._root, val)

    def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
        """递归删除节点（辅助方法）"""
        if node is None:
            return None
        # 1. 查找节点并删除
        if val < node.val:
            node.left = self.remove_helper(node.left, val)
        elif val > node.val:
            node.right = self.remove_helper(node.right, val)
        else:
            if node.left is None or node.right is None:
                child = node.left or node.right
                # 子节点数量 = 0 ，直接删除 node 并返回
                if child is None:
                    return None
                # 子节点数量 = 1 ，直接删除 node
                else:
                    node = child
            else:
                # 子节点数量 = 2 ，则将中序遍历的下个节点删除，并用该节点替换当前节点
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.right = self.remove_helper(node.right, temp.val)
                node.val = temp.val
        # 更新节点高度
        self.update_height(node)
        # 2. 执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)

    def pre_order(self) -> list[int]:
        """前序遍历"""
        res = []
        self.pre_order_helper(self._root, res)
        return res

    def pre_order_helper(self, node: TreeNode | None, res: list[int]):
        """递归前序遍历（辅助方法）"""
        if node:
            res.append(node.val)
            self.pre_order_helper(node.left, res)
            self.pre_order_helper(node.right, res)

    def in_order(self) -> list[int]:
        """中序遍历"""
        res = []
        self.in_order_helper(self._root, res)
        return res

    def in_order_helper(self, node: TreeNode | None, res: list[int]):
        """递归中序遍历（辅助方法）"""
        if node:
            self.in_order_helper(node.left, res)
            res.append(node.val)
            self.in_order_helper(node.right, res)

    def post_order(self) -> list[int]:
        """后序遍历"""
        res = []
        self.post_order_helper(self._root, res)
        return res

    def post_order_helper(self, node: TreeNode | None, res: list[int]):
        """递归后序遍历（辅助方法）"""
        if node:
            self.post_order_helper(node.left, res)
            self.post_order_helper(node.right, res)
            res.append(node.val)


# 示例使用
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(25)

print("前序遍历:", avl_tree.pre_order())
print("中序遍历:", avl_tree.in_order())
print("后序遍历:", avl_tree.post_order())

avl_tree.remove(40)
print("中序遍历 (删除40后):", avl_tree.in_order())
