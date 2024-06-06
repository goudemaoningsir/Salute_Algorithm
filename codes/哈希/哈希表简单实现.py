class Pair:
    """键值对"""

    def __init__(self, key: int, val: str):
        # 初始化键值对
        self.key = key
        self.val = val


class ArrayHashMap:
    """基于数组实现的哈希表"""

    def __init__(self):
        """构造方法"""
        # 初始化数组，包含 100 个桶
        self.buckets: list[Pair | None] = [None] * 100

    @staticmethod
    def hash_func(key: int) -> int:
        """哈希函数"""
        # 计算哈希值，取模 100
        index = key % 100
        return index

    def get(self, key: int) -> str | None:
        """查询操作"""
        # 根据键计算哈希值获取索引
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        # 如果该索引处没有键值对，返回 None
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        """添加操作"""
        # 创建新的键值对
        pair = Pair(key, val)
        # 根据键计算哈希值获取索引，并将键值对存入数组
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """删除操作"""
        # 根据键计算哈希值获取索引，将该索引位置置为 None
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """获取所有键值对"""
        result: list[Pair] = []
        # 遍历数组，收集非 None 的键值对
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """获取所有键"""
        result = []
        # 遍历数组，收集所有键
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """获取所有值"""
        result = []
        # 遍历数组，收集所有值
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self):
        """打印哈希表"""
        # 遍历数组，打印所有非 None 的键值对
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)


# 运行示例
if __name__ == "__main__":
    # 创建一个哈希表
    hashmap = ArrayHashMap()

    # 添加键值对
    hashmap.put(1, "value1")
    hashmap.put(2, "value2")
    hashmap.put(102, "value102")  # 102 % 100 == 2，与键 2 冲突

    # 打印哈希表
    hashmap.print()
    # 输出：
    # 1 -> value1
    # 102 -> value102

    # 获取键值
    print(hashmap.get(1))  # 输出：value1
    print(hashmap.get(2))  # 输出：value102（因为键 2 的值被覆盖）
    print(hashmap.get(102))  # 输出：value102

    # 删除键值对
    hashmap.remove(1)
    hashmap.print()
    # 输出：
    # 102 -> value102

    # 获取所有键、值、键值对
    print(hashmap.key_set())  # 输出：[102]
    print(hashmap.value_set())  # 输出：[value102]
    print(hashmap.entry_set())  # 输出：[<__main__.Pair object at 0x...>]
