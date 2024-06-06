class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        """检查栈是否为空"""
        return self.top is None

    def push(self, data):
        """向栈中添加元素"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """从栈中移除元素"""
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        """获取栈顶元素"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data


# 创建一个栈
stack = Stack()

# 向栈中添加元素
stack.push(1)
stack.push(2)
stack.push(3)

# 获取栈顶元素
print(stack.peek())  # 输出: 3

# 从栈中移除元素
print(stack.pop())  # 输出: 3
print(stack.pop())  # 输出: 2
print(stack.pop())  # 输出: 1
