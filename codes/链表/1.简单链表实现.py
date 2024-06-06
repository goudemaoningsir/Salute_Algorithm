class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """插入新的节点"""
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def delete(self, data):
        """删除一个节点"""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    def find(self, data):
        """查找数据的第一个节点"""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur  # 返回找到的节点
            cur = cur.next
        return None  # 如果没有找到，返回 None

    def print_list(self):
        """打印链表"""
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()


# 创建一个链表并插入节点
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# 打印链表
linked_list.print_list()  # 输出: 1 2 3 4

# 删除节点
linked_list.delete(3)

# 再次打印链表
linked_list.print_list()  # 输出: 1 2 4
