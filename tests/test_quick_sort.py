"""pytest 测试：quick_sort / quick_sort_inplace"""

import random

import pytest

from quick_sort import quick_sort, quick_sort_inplace


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([9, 8, 7, 6], [6, 7, 8, 9]),
        ([3, 3, 1, 2, 1], [1, 1, 2, 3, 3]),
        ([-1, -5, 0, 3], [-5, -1, 0, 3]),
        (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
    ],
)
def test_ascending(raw, expected):
    assert quick_sort(raw) == expected


def test_reverse():
    assert quick_sort([5, 1, 4], reverse=True) == [5, 4, 1]


def test_sort_by_key():
    assert quick_sort(["banana", "apple", "kiwi"], key=len) == ["kiwi", "apple", "banana"]


def test_does_not_mutate_input():
    original = [3, 1, 2]
    quick_sort(original)
    assert original == [3, 1, 2]


def test_inplace_returns_none_and_sorts():
    data = [3, 1, 2]
    assert quick_sort_inplace(data) is None
    assert data == [1, 2, 3]


def test_matches_builtin_sorted_on_random_data():
    rng = random.Random(2024)
    for _ in range(50):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 200))]
        assert quick_sort(data) == sorted(data)


def test_matches_builtin_sorted_reversed_on_random_data():
    rng = random.Random(7)
    for _ in range(20):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        assert quick_sort(data, reverse=True) == sorted(data, reverse=True)


def test_sorted_and_reverse_sorted_input_does_not_blow_up():
    """三数取中 + 显式栈：极端输入不能退化成深递归。"""
    ascending = list(range(2000))
    descending = list(range(1999, -1, -1))
    assert quick_sort(ascending) == ascending
    assert quick_sort(descending) == ascending


def test_all_equal_elements():
    assert quick_sort([4] * 500) == [4] * 500


def test_two_elements():
    assert quick_sort([2, 1]) == [1, 2]
    assert quick_sort([1, 2]) == [1, 2]
