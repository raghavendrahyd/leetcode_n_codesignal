# Description: Given a positive integer n, return an array of all the integers in the range [1, n^2] in spiral order.
# SpiralNumbers leetcode 59 link: https://leetcode.com/problems/spiral-matrix-ii/


def solution(n):
    res = []
    for i in range(n):
        res.append(list(numpy.random.uniform(0, 1, n)))
    top = 0
    bottom = n
    left = 0
    right = n
    tofill = list(range(1, n * n + 1))
    idx_to_fill = 0
    while left < right and top < bottom:
        for i in range(left, right):
            res[top][i] = tofill[idx_to_fill]
            idx_to_fill += 1
        top += 1

        for i in range(top, bottom):
            res[i][right - 1] = tofill[idx_to_fill]
            idx_to_fill += 1
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            res[bottom - 1][i] = tofill[idx_to_fill]
            idx_to_fill += 1
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            res[i][left] = tofill[idx_to_fill]
            idx_to_fill += 1
        left += 1

    return res
