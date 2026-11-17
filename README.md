# lobework-sorting

一个演示常见排序算法的极简 Python 项目：干净的实现 + 完整的 pytest 测试 + 可直接运行的小 demo。

目前包含：**冒泡排序（Bubble Sort）** 和 **选择排序（Selection Sort）**。

## 环境要求

- Python 3.9 及以上

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/lobework/lobework.git
cd lobework

# 2. 运行演示
python bubble_sort.py       # 冒泡排序 demo
python selection_sort.py    # 选择排序 demo

# 3. 运行测试
pip install pytest
pytest
```

## 项目结构

```text
lobework/
├── bubble_sort.py             # 冒泡排序实现 + 命令行 demo
├── selection_sort.py          # 选择排序实现 + 命令行 demo
├── tests/
│   ├── test_bubble_sort.py   # 冒泡排序测试用例
│   └── test_selection_sort.py # 选择排序测试用例
├── pyproject.toml             # 项目元数据与 pytest 配置
├── .gitignore
└── README.md
```

## 冒泡排序（Bubble Sort）

```python
from bubble_sort import bubble_sort, bubble_sort_inplace

bubble_sort([5, 1, 4, 2, 8])                  # -> [1, 2, 4, 5, 8]
bubble_sort([1, 2, 3], reverse=True)           # -> [3, 2, 1]
bubble_sort(["banana", "kiwi"], key=len)      # -> ['kiwi', 'banana']

data = [3, 1, 2]
bubble_sort_inplace(data)
print(data)                                   # -> [1, 2, 3]
```

每一轮从前往后把相邻元素两两比较，遇到逆序（升序时即 `左 > 右`）就交换。当前未排序区间里最大的元素会像气泡一样「浮」到区间末尾并被固定下来；重复 `n - 1` 轮，整个序列就有序了。

实现里保留了冒泡排序最常用的一个优化：**如果某一轮没有发生任何交换，说明剩下的部分已经有序，直接提前退出**。所以完全有序的输入只需一轮、复杂度为 O(n)。

| 指标 | 值 |
| --- | --- |
| 最好时间复杂度（已有序） | O(n) |
| 平均时间复杂度 | O(n²) |
| 最坏时间复杂度 | O(n²) |
| 空间复杂度 | O(1)，原地 |
| 稳定性 | 稳定 |

## 选择排序（Selection Sort）

```python
from selection_sort import selection_sort, selection_sort_inplace

selection_sort([5, 1, 4, 2, 8])                  # -> [1, 2, 4, 5, 8]
selection_sort([1, 2, 3], reverse=True)          # -> [3, 2, 1]
selection_sort(["banana", "kiwi"], key=len)      # -> ['kiwi', 'banana']

data = [3, 1, 2]
selection_sort_inplace(data)
print(data)                                      # -> [1, 2, 3]
```

每一轮 i（从 0 到 n-2）：在未排序区间 `items[i..n-1]` 中找到关键字最小的元素下标，然后把它与 `items[i]` 交换。交换完成后，位置 i 上的元素就是最终应有的值，可以固定下来。重复 `n - 1` 轮，整个序列就有序了。

与冒泡排序不同，选择排序每轮只做**一次交换**（在找到最小值后），而不是相邻两两交换，因此交换次数固定为 `n - 1` 次。

| 指标 | 值 |
| --- | --- |
| 最好时间复杂度 | O(n²) |
| 平均时间复杂度 | O(n²) |
| 最坏时间复杂度 | O(n²) |
| 空间复杂度 | O(1)，原地 |
| 稳定性 | 不稳定（交换可能跨越相等元素） |

## 共同支持的参数

两个算法的两个函数（返回新列表版 / 原地版）都支持：

- `reverse=True`：降序排列
- `key=...`：指定排序关键字，例如 `key=len` 按字符串长度排序、`key=lambda x: x["age"]` 按字典字段排序

## 命令行入口

安装后可直接通过命令行运行 demo：

```bash
pip install .
bubble-sort
selection-sort
```

> 这些排序算法主要用于教学和理解算法思想。实际业务排序请直接用 Python 内置的 `sorted()` / `list.sort()`（底层是 Timsort，最坏 O(n log n)）。

## 后续可扩展

- [ ] 加入插入排序、归并排序等算法做对比
- [ ] 打印每轮中间状态，做成可视化动画
- [ ] 用 `pytest-benchmark` 对不同算法做性能对比
