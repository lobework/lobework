"""选择排序（Selection Sort）的纯 Python 实现。

选择排序是一种直观的比较排序算法：每一轮从未排序区间中选出
最小（升序时）的元素，把它交换到未排序区间的最前面，然后
缩小未排序区间，重复 n - 1 轮即可完成排序。

与冒泡排序不同，选择排序每轮只做一次交换（在找到最小值后），
而不是相邻两两交换，因此交换次数固定为 n - 1 次。

特性小结：
- 时间复杂度：最好 / 平均 / 最坏均为 O(n^2)
- 空间复杂度：O(1)，原地排序
- 稳定性：不稳定（交换可能跨越相等元素）
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, MutableSequence
from typing import Any, TypeVar

T = TypeVar("T")

#: 取排序关键字，例如 key=len 表示按长度排序；None 表示直接比较元素本身。
KeyFunc = Callable[[Any], Any] | None


def selection_sort(
    items: Iterable[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> list[T]:
    """返回排序后的新列表，不修改传入的可迭代对象。

    >>> selection_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    >>> selection_sort([5, 1, 4], reverse=True)
    [5, 4, 1]
    >>> selection_sort(["banana", "kiwi", "apple"], key=len)
    ['kiwi', 'apple', 'banana']
    """
    result = list(items)
    selection_sort_inplace(result, reverse=reverse, key=key)
    return result


def selection_sort_inplace(
    items: MutableSequence[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> None:
    """原地选择排序，直接修改传入的序列，返回 None。

    每一轮 i（从 0 到 n-2）：
      1. 在未排序区间 items[i..n-1] 中找到关键字最小的元素下标 min_idx
      2. 把 items[i] 与 items[min_idx] 交换
    交换完成后，位置 i 上的元素就是最终应有的值，可以固定下来。
    """
    n = len(items)
    get_key = key if key is not None else (lambda item: item)

    for i in range(n - 1):
        # 在未排序区间 [i, n) 中找最小（或最大）元素的下标
        extremum_idx = i
        for j in range(i + 1, n):
            current = get_key(items[j])
            extremum = get_key(items[extremum_idx])
            should_update = current > extremum if reverse else current < extremum
            if should_update:
                extremum_idx = j
        # 把找到的极值交换到未排序区间的最前面
        if extremum_idx != i:
            items[i], items[extremum_idx] = items[extremum_idx], items[i]


def main() -> None:
    """命令行小 demo：python selection_sort.py"""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", numbers)
    selection_sort_inplace(numbers)
    print("升序结果:", numbers)

    words = ["banana", "apple", "kiwi"]
    print("按长度排序:", selection_sort(words, key=len))
    print("降序结果:", selection_sort(numbers, reverse=True))


if __name__ == "__main__":
    main()
