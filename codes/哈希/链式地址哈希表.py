class Pair:
    """键值对"""

    def __init__(self, key: int, val: str):
        # 初始化键值对
        self.key = key
        self.val = val


class HashMapChaining:
    """链式地址哈希表"""

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        # 初始化桶数组，每个桶是一个列表，用于存储冲突的键值对
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        # 计算哈希值，取模容量
        return key % self.capacity

    def load_factor(self) -> float:
        """负载因子"""
        # 计算当前负载因子
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """查询操作"""
        # 根据键计算哈希值获取索引
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若找到 key ，则返回对应 val
        for pair in bucket:
            if pair.key == key:
                return pair.val
        # 若未找到 key ，则返回 None
        return None

    def put(self, key: int, val: str):
        """添加操作"""
        # 当负载因子超过阈值时，执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若遇到指定 key ，则更新对应 val 并返回
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        # 若无该 key ，则将键值对添加至尾部
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        # 根据键计算哈希值获取索引
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，从中删除键值对
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        """扩容哈希表"""
        # 暂存原哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        """打印哈希表"""
        # 遍历所有桶，打印桶中的键值对
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
            print(res)


# 运行示例
if __name__ == "__main__":
    # 创建一个哈希表
    hashmap = HashMapChaining()

    # 添加键值对
    hashmap.put(1, "value1")
    hashmap.put(2, "value2")
    hashmap.put(6, "value6")  # 6 % 4 == 2，与键 2 冲突
    hashmap.put(10, "value10")  # 10 % 4 == 2，与键 2 冲突

    print("==================== 打印哈希表 ==================== ")
    hashmap.print()

    print("==================== 获取键值 ==================== ")
    print(hashmap.get(1))  # 输出：value1
    print(hashmap.get(2))  # 输出：value2
    print(hashmap.get(6))  # 输出：value6
    print(hashmap.get(10))  # 输出：value10

    print("==================== 删除键值对 ==================== ")
    hashmap.remove(6)
    hashmap.print()

    print("==================== 添加更多键值对，触发扩容 ==================== ")
    hashmap.put(3, "value3")
    hashmap.put(7, "value7")
    hashmap.put(11, "value11")

    # 打印哈希表
    hashmap.print()

