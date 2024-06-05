from typing import Optional


class ListNode:
    """双向链表节点"""

    def __init__(self, val: int) -> None:
        """构造方法"""
        self.val: int = val
        self.next: Optional[ListNode] = None  # 后继节点引用（指针）
        self.prev: Optional[ListNode] = None  # 前驱节点引用（指针）


class LinkedListDeque:
    """基于双向链表实现的双向队列"""

    def __init__(self) -> None:
        """构造方法"""
        self.front: Optional[ListNode] = None  # 头节点 front
        self.rear: Optional[ListNode] = None  # 尾节点 rear
        self.__size: int = 0  # 双向队列的长度

    def size(self) -> int:
        """获取双向队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断双向队列是否为空"""
        return self.size() == 0

    def push(self, num: int, is_front: bool) -> None:
        """入队操作"""
        node = ListNode(num)
        # 若链表为空，则令 front, rear 都指向 node
        if self.is_empty():
            self.front = self.rear = node
        # 队首入队操作
        elif is_front:
            # 将 node 添加至链表头部
            self.front.prev = node
            node.next = self.front
            self.front = node  # 更新头节点
        # 队尾入队操作
        else:
            # 将 node 添加至链表尾部
            self.rear.next = node
            node.prev = self.rear
            self.rear = node  # 更新尾节点
        self.__size += 1  # 更新队列长度

    def push_first(self, num: int) -> None:
        """队首入队"""
        self.push(num, True)

    def push_last(self, num: int) -> None:
        """队尾入队"""
        self.push(num, False)

    def pop(self, is_front: bool) -> Optional[int]:
        """出队操作"""
        # 若队列为空，直接返回 None
        if self.is_empty():
            return None
        # 队首出队操作
        if is_front:
            val: int = self.front.val  # 暂存头节点值
            # 删除头节点
            fnext: Optional[ListNode] = self.front.next
            if fnext != None:
                fnext.prev = None
                self.front.next = None
            self.front = fnext  # 更新头节点
        # 队尾出队操作
        else:
            val: int = self.rear.val  # 暂存尾节点值
            # 删除尾节点
            rprev: Optional[ListNode] = self.rear.prev
            if rprev != None:
                rprev.next = None
                self.rear.prev = None
            self.rear = rprev  # 更新尾节点
        self.__size -= 1  # 更新队列长度
        return val

    def pop_first(self) -> int:
        """队首出队"""
        return self.pop(True)

    def pop_last(self) -> int:
        """队尾出队"""
        return self.pop(False)

    def peek_first(self) -> int:
        """访问队首元素"""
        return None if self.is_empty() else self.front.val

    def peek_last(self) -> int:
        """访问队尾元素"""
        return None if self.is_empty() else self.rear.val

    def to_array(self) -> list[int]:
        """返回数组用于打印"""
        node = self.front
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res


# 创建一个双向队列
deque = LinkedListDeque()

# 向队首和队尾添加元素
deque.push_first(1)
deque.push_last(2)
print(deque.to_array())  # 输出: [1, 2]

# 查看双向队列是否为空
print(deque.is_empty())  # 输出: False

# 查看双向队列的长度
print(deque.size())  # 输出: 2

# 查看队首和队尾元素
print(deque.peek_first())  # 输出: 1
print(deque.peek_last())  # 输出: 2

# 队首和队尾出队
print(deque.pop_first())  # 输出: 1
print(deque.pop_last())  # 输出: 2
print(deque.to_array())  # 输出: []

# 再次向队首和队尾添加元素
deque.push_first(3)
deque.push_last(4)
print(deque.to_array())  # 输出: [3, 4]
