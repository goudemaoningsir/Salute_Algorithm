from collections import deque
from typing import List


class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


class BinaryTree:
    """二叉树类"""

    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, val: int) -> None:
        """插入新节点"""
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node: TreeNode, val: int) -> None:
        """递归插入新节点"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def search(self, val: int) -> bool:
        """搜索节点"""
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node: TreeNode | None, val: int) -> bool:
        """递归搜索节点"""
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def delete(self, val: int) -> None:
        """删除节点"""
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node: TreeNode | None, val: int) -> TreeNode | None:
        """递归删除节点"""
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
        return node

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """找到最小值节点"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self) -> list[int]:
        """中序遍历"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: TreeNode | None, result: list[int]) -> None:
        """递归中序遍历"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

    def level_order(self) -> List[int]:
        """层序遍历"""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def pre_order(self, node: TreeNode | None, result: list[int]) -> None:
        """前序遍历"""
        if node is None:
            return
        result.append(node.val)
        self.pre_order(node.left, result)
        self.pre_order(node.right, result)

    def in_order(self, node: TreeNode | None, result: list[int]) -> None:
        """中序遍历"""
        if node is None:
            return
        self.in_order(node.left, result)
        result.append(node.val)
        self.in_order(node.right, result)

    def post_order(self, node: TreeNode | None, result: list[int]) -> None:
        """后序遍历"""
        if node is None:
            return
        self.post_order(node.left, result)
        self.post_order(node.right, result)
        result.append(node.val)


# 示例使用
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 中序遍历
print(bt.inorder())  # 输出 [2, 3, 4, 5, 6, 7, 8]

# 搜索节点
print(bt.search(4))  # 输出 True
print(bt.search(9))  # 输出 False

# 删除节点
bt.delete(5)
print(bt.inorder())  # 输出 [2, 3, 4, 6, 7, 8]

# 层序遍历
print(bt.level_order())  # 输出 [6, 3, 7, 2, 4, 8]

# 前序遍历
pre_order_result = []
bt.pre_order(bt.root, pre_order_result)
print(pre_order_result)  # 输出 [6, 3, 2, 4, 7, 8]

# 中序遍历
in_order_result = []
bt.in_order(bt.root, in_order_result)
print(in_order_result)  # 输出 [2, 3, 4, 6, 7, 8]

# 后序遍历
post_order_result = []
bt.post_order(bt.root, post_order_result)
print(post_order_result)  # 输出 [2, 4, 3, 8, 7, 6]
