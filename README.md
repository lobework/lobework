# bubble-sort

一个演示 **冒泡排序（Bubble Sort）** 与 **快速排序（Quick Sort）** 的 Python 项目：干净的实现 + 完整的 pytest 测试 + 可直接运行的小 demo。

## 环境要求

- Python 3.9 及以上

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/lobework/lobework.git
cd lobework

# 2. 直接运行演示
python bubble_sort.py
python quick_sort.py

# 3. 运行测试
pip install pytest
pytest
```

冒泡排序演示输出：

```text
原始列表: [64, 34, 25, 12, 22, 11, 90]
升序结果: [11, 12, 22, 25, 34, 64, 90]
按长度排序: ['kiwi', 'apple', 'banana']
降序结果: [90, 64, 34, 25, 22, 12, 11]
```

## 项目结构

```text
lobework/
├── bubble_sort.py             # 冒泡排序实现 + 命令行 demo
├── quick_sort.py              # 快速排序实现 + 命令行 demo
├── tests/
│   ├── test_bubble_sort.py    # 冒泡排序测试
│   └── test_quick_sort.py     # 快速排序测试
├── pyproject.toml             # 项目元数据与 pytest 配置
├── .gitignore
└── README.md
```

## 使用方式

两个模块的 API 保持一致，都提供「返回新列表」和「原地排序」两种形式：

```python
from bubble_sort import bubble_sort, bubble_sort_inplace
from quick_sort import quick_sort, quick_sort_inplace

# 返回新列表，原数据不变
bubble_sort([5, 1, 4, 2, 8])                  # -> [1, 2, 4, 5, 8]
quick_sort([5, 1, 4, 2, 8])                   # -> [1, 2, 4, 5, 8]
quick_sort([1, 2, 3], reverse=True)           # -> [3, 2, 1]
quick_sort(["banana", "kiwi"], key=len)       # -> ['kiwi', 'banana']

# 原地排序，直接改传入的列表，返回 None
data = [3, 1, 2]
quick_sort_inplace(data)
print(data)                                   # -> [1, 2, 3]
```

所有函数都支持：

- `reverse=True`：降序排列
- `key=...`：指定排序关键字，例如 `key=len` 按字符串长度、`key=lambda x: x["age"]` 按字典字段

## 算法说明

### 冒泡排序

每一轮从前往后把相邻元素两两比较，遇到逆序（升序时即 `左 > 右`）就交换。当前未排序区间里最大的元素会像气泡一样「浮」到区间末尾并被固定下来；重复 `n - 1` 轮，整个序列有序。实现里保留了常用优化：**某一轮没有发生任何交换就提前退出**，因此完全有序的输入只需一轮、复杂度 O(n)。

### 快速排序

分治：选一个基准（pivot），把区间划分成「不大于基准」和「大于基准」两段，再分别处理两段。实现里做了两点工程优化：

1. **三数取中**：在区间首、中、尾取中间值作基准，缓解已排序 / 逆序输入退化成 O(n²) 的问题；
2. **显式栈 + 优先处理短段**：用栈代替递归，并且只把较长的一段压栈，把栈深控制在 O(log n)，极端输入也不会递归过深。

注意：快速排序是**不稳定**的排序算法（相等元素的相对顺序可能改变）。

### 复杂度对比

| 算法 | 最好 | 平均 | 最坏 | 空间 | 稳定性 |
| --- | --- | --- | --- | --- | --- |
| 冒泡排序 | O(n) | O(n²) | O(n²) | O(1)，原地 | 稳定 |
| 快速排序 | O(n log n) | O(n log n) | O(n²) | O(log n)，栈 | 不稳定 |

> 两者主要用于教学和理解算法思想。实际业务排序请直接用 Python 内置的 `sorted()` / `list.sort()`（底层是 Timsort，最坏 O(n log n) 且稳定）。

## 后续可扩展

- [x] 加入快速排序做对比
- [ ] 加入插入排序、归并排序等算法做对比
- [ ] 打印每轮中间状态，做成可视化动画
- [ ] 用 `pytest-benchmark` 对不同算法做性能对比
