class Pair:
    """键值对"""

    def __init__(self, key: int, val: str):
        # 初始化键值对
        self.key = key
        self.val = val


class HashMapOpenAddressing:
    """开放寻址哈希表"""

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets: list[Pair | None] = [None] * self.capacity  # 桶数组
        self.TOMBSTONE = Pair(-1, "-1")  # 删除标记

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        # 计算哈希值，取模容量
        return key % self.capacity

    def load_factor(self) -> float:
        """负载因子"""
        # 计算当前负载因子
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        """搜索 key 对应的桶索引"""
        index = self.hash_func(key)
        first_tombstone = -1
        # 线性探测，当遇到空桶时跳出
        while self.buckets[index] is not None:
            # 若遇到 key ，返回对应的桶索引
            if self.buckets[index].key == key:
                # 若之前遇到了删除标记，则将键值对移动至该索引处
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone  # 返回移动后的桶索引
                return index  # 返回桶索引
            # 记录遇到的首个删除标记
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            # 计算桶索引，越过尾部则返回头部
            index = (index + 1) % self.capacity
        # 若 key 不存在，则返回添加点的索引
        return index if first_tombstone == -1 else first_tombstone

    def get(self, key: int) -> str | None:
        """查询操作"""
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 若找到键值对，则返回对应 val
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        # 若键值对不存在，则返回 None
        return None

    def put(self, key: int, val: str):
        """添加操作"""
        # 当负载因子超过阈值时，执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 若找到键值对，则覆盖 val 并返回
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        # 若键值对不存在，则添加该键值对
        self.buckets[index] = Pair(key, val)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 若找到键值对，则用删除标记覆盖它
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def extend(self):
        """扩容哈希表"""
        # 暂存原哈希表
        buckets_tmp = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for pair in buckets_tmp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.val)


# 运行示例
if __name__ == "__main__":
    # 创建一个哈希表
    hashmap = HashMapOpenAddressing()

    print("=================== 添加键值对 ===================")
    hashmap.put(1, "value1")
    hashmap.put(2, "value2")
    hashmap.put(6, "value6")  # 6 % 4 == 2，与键 2 冲突
    hashmap.put(10, "value10")  # 10 % 4 == 2，与键 2 冲突

    # 打印哈希表
    print("哈希表内容：")
    hashmap.print()
    # 输出：
    # None
    # 1 -> value1
    # 2 -> value2
    # None

    print("=================== 获取键值 ===================")
    print("\n查询操作：")
    print(hashmap.get(1))  # 输出：value1
    print(hashmap.get(2))  # 输出：value2
    print(hashmap.get(6))  # 输出：value6
    print(hashmap.get(10))  # 输出：value10

    # 删除键值对
    print("\n删除键6后的哈希表内容：")
    hashmap.remove(6)
    hashmap.print()
    # 输出：
    # None
    # 1 -> value1
    # 2 -> value2
    # None

    # 添加更多键值对，触发扩容
    print("\n触发扩容后的哈希表内容：")
    hashmap.put(3, "value3")
    hashmap.put(7, "value7")
    hashmap.put(11, "value11")
    hashmap.print()
    # 输出：
    # None
    # 1 -> value1
    # 2 -> value2
    # None
    # None
    # 3 -> value3
    # 7 -> value7
    # 11 -> value11
