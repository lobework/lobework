"""冒泡排序（Bubble Sort）的纯 Python 实现。

冒泡排序是最容易理解的交换排序算法：每轮把相邻元素两两比较，
逆序就交换，于是未排序区间里最大（升序时）的元素会像气泡一样
"浮"到区间末尾，重复 n - 1 轮即可完成排序。

特性小结：
- 时间复杂度：最好 O(n)（已有序时配合提前退出），平均 / 最坏 O(n^2)
- 空间复杂度：O(1)，原地排序
- 稳定性：稳定（相等元素不会改变相对顺序）
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, MutableSequence
from typing import Any, TypeVar

T = TypeVar("T")

#: 取排序关键字，例如 key=len 表示按长度排序；None 表示直接比较元素本身。
KeyFunc = Callable[[Any], Any] | None


def bubble_sort(
    items: Iterable[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> list[T]:
    """返回排序后的新列表，不修改传入的可迭代对象。

    >>> bubble_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    >>> bubble_sort([5, 1, 4], reverse=True)
    [5, 4, 1]
    >>> bubble_sort(["banana", "kiwi", "apple"], key=len)
    ['kiwi', 'apple', 'banana']
    """
    result = list(items)
    bubble_sort_inplace(result, reverse=reverse, key=key)
    return result


def bubble_sort_inplace(
    items: MutableSequence[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> None:
    """原地冒泡排序，直接修改传入的序列，返回 None。

    每轮结束后区间末尾就固定了一个元素，所以下一轮只需要扫描
    0 .. end-1。另外，如果某一轮没有任何交换，说明剩下的部分
    已经有序，可以提前退出（这正是最好的 O(n) 情况）。
    """
    n = len(items)
    get_key = key if key is not None else (lambda item: item)

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            left = get_key(items[i])
            right = get_key(items[i + 1])
            should_swap = left < right if reverse else left > right
            if should_swap:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break


def main() -> None:
    """命令行小 demo：python bubble_sort.py"""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", numbers)
    bubble_sort_inplace(numbers)
    print("升序结果:", numbers)

    words = ["banana", "apple", "kiwi"]
    print("按长度排序:", bubble_sort(words, key=len))
    print("降序结果:", bubble_sort(numbers, reverse=True))


if __name__ == "__main__":
    main()
