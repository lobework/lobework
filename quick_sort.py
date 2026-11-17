"""快速排序（Quick Sort）的纯 Python 实现。

快速排序采用分治思路：选一个基准（pivot），把序列划分成
"不大于基准" 和 "大于基准" 两段，再对两段分别处理，
平均复杂度 O(n log n)，是实践中最常用的通用排序算法之一。

实现里做了两点工程优化：
- **三数取中** 选基准，缓解已排序 / 逆序输入退化成 O(n^2) 的问题；
- **显式栈** 代替递归，并且总是先处理较短的一段、把较长的一段压栈，
  把栈深控制在 O(log n)，避免极端输入下的递归过深。

注意：与冒泡排序不同，快速排序是**不稳定**的排序算法。
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, MutableSequence
from typing import Any, TypeVar

T = TypeVar("T")

#: 取排序关键字，例如 key=len 表示按长度排序；None 表示直接比较元素本身。
KeyFunc = Callable[[Any], Any] | None
_KeyFunc = Callable[[Any], Any]


def quick_sort(
    items: Iterable[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> list[T]:
    """返回排序后的新列表，不修改传入的可迭代对象。

    >>> quick_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    >>> quick_sort([5, 1, 4], reverse=True)
    [5, 4, 1]
    >>> quick_sort(["banana", "kiwi", "apple"], key=len)
    ['kiwi', 'apple', 'banana']
    """
    result = list(items)
    quick_sort_inplace(result, reverse=reverse, key=key)
    return result


def quick_sort_inplace(
    items: MutableSequence[T],
    *,
    reverse: bool = False,
    key: KeyFunc = None,
) -> None:
    """原地快速排序，直接修改传入的序列，返回 None。"""
    n = len(items)
    if n < 2:
        return

    get_key: _KeyFunc = key if key is not None else (lambda item: item)
    stack: list[tuple[int, int]] = [(0, n - 1)]

    while stack:
        low, high = stack.pop()
        while low < high:
            pivot_index = _partition(items, low, high, get_key, reverse)
            # 较短的一段继续留在当前循环里处理，较长的一段才压栈，
            # 因此栈的最大深度只有 O(log n)。
            if pivot_index - low < high - pivot_index:
                if pivot_index + 1 < high:
                    stack.append((pivot_index + 1, high))
                high = pivot_index - 1
            else:
                if low < pivot_index - 1:
                    stack.append((low, pivot_index - 1))
                low = pivot_index + 1


def _partition(
    items: MutableSequence[T],
    low: int,
    high: int,
    get_key: _KeyFunc,
    reverse: bool,
) -> int:
    """Lomuto 划分：把基准归位并返回它的最终下标。"""
    mid = (low + high) // 2
    median = _median_of_three(items, low, mid, high, get_key, reverse)
    items[low], items[median] = items[median], items[low]

    pivot = get_key(items[low])
    boundary = low + 1  # 下一个「应放到基准左侧」的位置
    for j in range(low + 1, high + 1):
        value = get_key(items[j])
        goes_left = value >= pivot if reverse else value <= pivot
        if goes_left:
            items[boundary], items[j] = items[j], items[boundary]
            boundary += 1

    items[low], items[boundary - 1] = items[boundary - 1], items[low]
    return boundary - 1


def _median_of_three(
    items: MutableSequence[T],
    a: int,
    b: int,
    c: int,
    get_key: _KeyFunc,
    reverse: bool,
) -> int:
    """返回三个下标里「按当前排序方向属于中间值」的那个下标。"""
    ka, kb, kc = get_key(items[a]), get_key(items[b]), get_key(items[c])
    before = (lambda x, y: x > y) if reverse else (lambda x, y: x < y)

    if before(ka, kb):
        if before(kb, kc):
            return b
        return c if before(ka, kc) else a
    if before(ka, kc):
        return a
    return c if before(kb, kc) else b


def main() -> None:
    """命令行小 demo：python quick_sort.py"""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", numbers)
    quick_sort_inplace(numbers)
    print("升序结果:", numbers)
    print("降序结果:", quick_sort(numbers, reverse=True))

    words = ["banana", "apple", "kiwi"]
    print("按长度排序:", quick_sort(words, key=len))


if __name__ == "__main__":
    main()
