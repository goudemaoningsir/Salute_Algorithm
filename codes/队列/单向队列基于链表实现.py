class Node:
    def __init__(self, data):
        self.data = data  # 节点的数据
        self.next = None  # 指向下一个节点的指针


class Queue:
    def __init__(self):
        self.front = self.rear = None  # 队列的前端和后端初始化为空

    def is_empty(self):
        """检查队列是否为空"""
        return self.front is None

    def enqueue(self, item):
        """向队列添加元素"""
        temp = Node(item)  # 创建新节点

        if self.rear is None:  # 如果队列为空
            self.front = self.rear = temp  # 新节点为前端和后端
            return
        self.rear.next = temp  # 将新节点链接到队列的后端
        self.rear = temp  # 更新队列的后端为新节点

    def dequeue(self):
        """从队列移除元素"""
        if self.is_empty():  # 如果队列为空，返回 None
            return
        temp = self.front  # 保存前端节点
        self.front = temp.next  # 更新前端为下一个节点

        if self.front is None:  # 如果队列变为空
            self.rear = None  # 将后端设为空

        return str(temp.data)  # 返回移除的节点的数据

    def peek(self):
        """获取队列的第一个元素"""
        if self.is_empty():  # 如果队列为空，返回 None
            return
        return str(self.front.data)  # 返回前端节点的数据


# 创建一个队列
q = Queue()

# 向队列添加元素
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# 获取队列的第一个元素
print(q.peek())  # 输出: 1

# 从队列移除元素
print(q.dequeue())  # 输出: 1
print(q.dequeue())  # 输出: 2
print(q.dequeue())  # 输出: 3
