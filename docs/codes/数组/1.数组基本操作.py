from util import log_operation
import random


@log_operation
def create_array(value, size):
    """创建一个指定大小的数组（列表）"""
    return [value] * size


# 创建一个包含 5 个元素的数组
arr = create_array(None, 5)


# # 创建一个包含初始元素的数组
# arr = [1, 2, 3, 4, 5]
# print("初始数组:", arr)  # 初始数组: [1, 2, 3, 4, 5]


@log_operation
def random_access(nums: list[int]) -> int:
    """随机访问数组中的一个元素"""
    # 在区间 [0, len(nums)-1] 中随机选择一个索引
    random_index = random.randint(0, len(nums) - 1)
    # 根据随机索引获取并返回数组中的元素
    random_num = nums[random_index]
    return random_num


# 调用 random_access 函数
random_element = random_access([10, 20, 30, 40, 50])


@log_operation
def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋给 index 处的元素
    nums[index] = num
    return nums


# 调用 insert 函数
insert([1, 2, 3, 5, 6], 4, 3)


@log_operation
def remove(nums: list[int], index: int):
    """删除索引 index 处的元素"""
    # 确保索引 index 在数组的有效范围内
    if index < 0 or index >= len(nums):
        raise IndexError("索引超出数组范围")

    # 把索引 index 之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

    # 移除数组中的最后一个元素
    del nums[-1]

    return nums


# 调用 remove 函数
remove([1, 2, 3, 4, 5, 6], 2)


@log_operation
def traverse(nums: list[int]) -> int:
    """遍历数组并计算元素总和"""
    count = 0  # 初始化计数器为0

    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]  # 累加每个元素的值

    # 直接遍历数组元素（这个循环是多余的，因为上面的循环已经计算了总和）
    # for num in nums:
    #     count += num

    # 同时遍历数据索引和元素（这个循环同样是多余的）
    # for i, num in enumerate(nums):
    #     count += nums[i]  # 这会重复累加
    #     count += num      # 这会再次重复累加

    return count  # 返回总和


# 调用 traverse 函数
total = traverse([1, 2, 3, 4, 5])


@log_operation
def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# 演示数据
nums = [5, 3, 7, 1, 9, 8]
target = 7

# 调用 find 函数
index = find(nums, target)

# 输出结果
if index != -1:
    print(f"找到目标元素 {target} 在索引 {index}")
else:
    print(f"未找到目标元素 {target}")


@log_operation
def extend(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的新数组
    return res


# 调用 extend 函数
extended_nums = extend([1, 2, 3], 3)
