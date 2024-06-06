class ArrayDeque:
    """基于环形数组实现的双向队列"""

    def __init__(self, capacity: int) -> None:
        """构造方法"""
        self.__nums: list[int] = [0] * capacity
        self.__front: int = 0
        self.__size: int = 0

    def capacity(self) -> int:
        """获取双向队列的容量"""
        return len(self.__nums)

    def size(self) -> int:
        """获取双向队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断双向队列是否为空"""
        return self.__size == 0

    def index(self, i: int) -> int:
        """计算环形数组索引"""
        # 通过取余操作实现数组首尾相连
        # 当 i 越过数组尾部后，回到头部
        # 当 i 越过数组头部后，回到尾部
        return (i + self.capacity()) % self.capacity()

    def push_first(self, num: int) -> None:
        """队首入队"""
        if self.__size == self.capacity():
            print("双向队列已满")
            return
        # 队首指针向左移动一位
        # 通过取余操作，实现 front 越过数组头部后回到尾部
        self.__front = self.index(self.__front - 1)
        # 将 num 添加至队首
        self.__nums[self.__front] = num
        self.__size += 1

    def push_last(self, num: int) -> None:
        """队尾入队"""
        if self.__size == self.capacity():
            print("双向队列已满")
            return
        # 计算尾指针，指向队尾索引 + 1
        rear = self.index(self.__front + self.__size)
        # 将 num 添加至队尾
        self.__nums[rear] = num
        self.__size += 1

    def pop_first(self) -> int:
        """队首出队"""
        num = self.peek_first()
        # 队首指针向后移动一位
        self.__front = self.index(self.__front + 1)
        self.__size -= 1
        return num

    def pop_last(self) -> int:
        """队尾出队"""
        num = self.peek_last()
        self.__size -= 1
        return num

    def peek_first(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self.__nums[self.__front]

    def peek_last(self) -> int:
        """访问队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        # 计算尾元素索引
        last = self.index(self.__front + self.__size - 1)
        return self.__nums[last]

    def to_array(self) -> list[int]:
        """返回数组用于打印"""
        # 仅转换有效长度范围内的列表元素
        res = []
        for i in range(self.__size):
            res.append(self.__nums[self.index(self.__front + i)])
        return res


# 创建一个双向队列
deque = ArrayDeque(5)

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
