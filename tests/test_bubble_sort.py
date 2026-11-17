"""pytest 测试：bubble_sort / bubble_sort_inplace"""

import random

import pytest

from bubble_sort import bubble_sort, bubble_sort_inplace


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
    assert bubble_sort(raw) == expected


def test_reverse():
    assert bubble_sort([5, 1, 4], reverse=True) == [5, 4, 1]


def test_sort_by_key():
    assert bubble_sort(["banana", "apple", "kiwi"], key=len) == ["kiwi", "apple", "banana"]


def test_is_stable():
    pairs = [(2, "a"), (1, "x"), (2, "b"), (1, "y")]
    assert bubble_sort(pairs, key=lambda pair: pair[0]) == [
        (1, "x"),
        (1, "y"),
        (2, "a"),
        (2, "b"),
    ]


def test_does_not_mutate_input():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]


def test_inplace_returns_none_and_sorts():
    data = [3, 1, 2]
    assert bubble_sort_inplace(data) is None
    assert data == [1, 2, 3]


def test_matches_builtin_sorted_on_random_data():
    rng = random.Random(2024)
    for _ in range(20):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 30))]
        assert bubble_sort(data) == sorted(data)
