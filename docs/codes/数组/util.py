# !/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import pprint
from functools import wraps


def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"================ {func.__name__} 函数 开始执行 ================")
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)
        end_time = time.time()  # 记录结束时间
        runtime = end_time - start_time  # 计算运行时间
        print(f"================ {func.__name__} 函数 结束执行================")
        pprint.pprint(result)
        print(f"{func.__name__} 函数运行时间：{runtime:.4f}秒")
        print(f"================ {func.__name__} 函数 返回结果================")
        return result

    return wrapper
