# bubble-sort

一个演示 **冒泡排序（Bubble Sort）** 的极简 Python 项目：干净的实现 + 完整的 pytest 测试 + 可直接运行的小 demo。

## 环境要求

- Python 3.9 及以上

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/lobework/lobework.git
cd lobework

# 2. 直接运行演示
python bubble_sort.py

# 3. 运行测试
pip install pytest
pytest
```

演示输出：

```text
原始列表: [64, 34, 25, 12, 22, 11, 90]
升序结果: [11, 12, 22, 25, 34, 64, 90]
按长度排序: ['kiwi', 'apple', 'banana']
降序结果: [90, 64, 34, 25, 22, 12, 11]
```

## 项目结构

```text
lobework/
├── bubble_sort.py             # 算法实现 + 命令行 demo
├── tests/
│   └── test_bubble_sort.py    # pytest 测试用例
├── pyproject.toml             # 项目元数据与 pytest 配置
├── .gitignore
└── README.md
```

## 使用方式

```python
from bubble_sort import bubble_sort, bubble_sort_inplace

# 返回新列表，原数据不变
bubble_sort([5, 1, 4, 2, 8])                  # -> [1, 2, 4, 5, 8]
bubble_sort([1, 2, 3], reverse=True)          # -> [3, 2, 1]
bubble_sort(["banana", "kiwi"], key=len)      # -> ['kiwi', 'banana']

# 原地排序，直接改传入的列表，返回 None
data = [3, 1, 2]
bubble_sort_inplace(data)
print(data)                                   # -> [1, 2, 3]
```

两个函数都支持：

- `reverse=True`：降序排列
- `key=...`：指定排序关键字，例如 `key=len` 按字符串长度排序、`key=lambda x: x["age"]` 按字典字段排序

## 算法说明

每一轮从前往后把相邻元素两两比较，遇到逆序（升序时即 `左 > 右`）就交换。这样一来，当前未排序区间里最大的元素会像气泡一样「浮」到区间末尾并被固定下来；重复 `n - 1` 轮，整个序列就有序了。

实现里保留了冒泡排序最常用的一个优化：**如果某一轮没有发生任何交换，说明剩下的部分已经有序，直接提前退出**。所以完全有序的输入只需一轮、复杂度为 O(n)。

| 指标 | 值 |
| --- | --- |
| 最好时间复杂度（已有序） | O(n) |
| 平均时间复杂度 | O(n²) |
| 最坏时间复杂度 | O(n²) |
| 空间复杂度 | O(1)，原地 |
| 稳定性 | 稳定 |

> 冒泡排序主要用于教学和理解算法思想。实际业务排序请直接用 Python 内置的 `sorted()` / `list.sort()`（底层是 Timsort，最坏 O(n log n)）。

## 后续可扩展

- [ ] 加入插入排序、归并排序等算法做对比
- [ ] 打印每轮中间状态，做成可视化动画
- [ ] 用 `pytest-benchmark` 对不同算法做性能对比
