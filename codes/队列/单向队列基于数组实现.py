class ArrayQueue:
    """基于环形数组实现的队列"""

    def __init__(self, size: int) -> None:
        """构造方法"""
        self.__nums: list[int] = [0] * size  # 用于存储队列元素的数组
        self.__front: int = 0  # 队首指针，指向队首元素
        self.__size: int = 0  # 队列长度

    def capacity(self) -> int:
        """获取队列的容量"""
        return len(self.__nums)

    def size(self) -> int:
        """获取队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self.__size == 0

    def push(self, num: int) -> None:
        """入队"""
        if self.__size == self.capacity():
            raise IndexError("队列已满")
        # 计算尾指针，指向队尾索引 + 1
        # 通过取余操作，实现 rear 越过数组尾部后回到头部F
        rear: int = (self.__front + self.__size) % self.capacity()
        # 将 num 添加至队尾
        self.__nums[rear] = num
        self.__size += 1

    def pop(self) -> int:
        """出队"""
        num: int = self.peek()
        # 队首指针向后移动一位，若越过尾部则返回到数组头部
        self.__front = (self.__front + 1) % self.capacity()
        self.__size -= 1
        return num

    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self.__nums[self.__front]

    def to_list(self) -> list[int]:
        """返回列表用于打印"""
        res = [0] * self.size()
        j: int = self.__front
        for i in range(self.size()):
            res[i] = self.__nums[(j % self.capacity())]
            j += 1
        return res


# 创建一个容量为5的队列
queue = ArrayQueue(5)

# 添加元素到队列
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.to_list())  # 输出: [1, 2, 3]

# 查看队列是否为空
print(queue.is_empty())  # 输出: False

# 查看队列的容量
print(queue.capacity())  # 输出: 5

# 查看队列的长度
print(queue.size())  # 输出: 3

# 查看队首元素
print(queue.peek())  # 输出: 1

# 出队
print(queue.pop())  # 输出: 1
print(queue.to_list())  # 输出: [2, 3]

# 再次入队
queue.push(4)
queue.push(5)
print(queue.to_list())  # 输出: [2, 3, 4, 5]

# 入队，由于队列已满，将抛出异常
try:
    queue.push(6)  # 抛出: IndexError: 队列已满
except IndexError as e:
    print(e)
