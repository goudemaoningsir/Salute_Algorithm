class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """检查栈是否为空"""
        return len(self.stack) == 0

    def push(self, data):
        """向栈中添加元素"""
        self.stack.append(data)

    def pop(self):
        """从栈中移除元素"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """获取栈顶元素"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]


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
